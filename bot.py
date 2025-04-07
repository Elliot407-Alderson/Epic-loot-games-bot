import telebot
from telebot import types
import requests

Токен бота
BOT_TOKEN = '7368021326:AAEnUn11ru-oPeOgEFUfQ9bWmDRy7OVDB1U'
bot = telebot.TeleBot(BOT_TOKEN)

Подписки (временно без БД)
user_genres = {}
user_games = {}

Получение бесплатных игр с Epic
def get_free_epic_games():
url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru-RU&country=RU&allowCountries=RU"
response = requests.get(url)
data = response.json()

games = []

for item in data['data']['Catalog']['searchStore']['elements']:
    if item['promotions'] and item['promotions'].get('promotionalOffers'):
        title = item['title']
        slug = item['productSlug'] or item['catalogNs']['mappings'][0]['pageSlug']
        link = f"https://store.epicgames.com/ru/p/{slug}"
        games.append({
            'name': title,
            'price': 'Бесплатно',
            'link': link
        })

return games
Получение игр со скидкой
def get_discounted_epic_games():
url = "https://www.cheapshark.com/api/1.0/deals?storeID=25&onSale=1"
response = requests.get(url)
data = response.json()

games = []

for item in data[:5]:  # первые 5 скидок
    title = item['title']
    sale_price = item['salePrice']
    normal_price = item['normalPrice']
    savings = round(float(item['savings']))
    link = f"https://www.cheapshark.com/redirect?dealID={item['dealID']}"

    games.append({
        'name': title,
        'price': f"{savings}% скидка — {sale_price}$ (было {normal_price}$)",
        'link': link
    })

return games
Стартовое меню
@bot.message_handler(commands=['start'])
def start_handler(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("Игры на распродаже", "Следить за жанром", "Следить за игрой")
bot.send_message(message.chat.id,
"Привет! Выбери, что хочешь сделать:",
reply_markup=markup)

Обработка кнопок
@bot.message_handler(func=lambda message: True)
def menu_handler(message):
if message.text == "Игры на распродаже":
show_sales_overview(message)

elif message.text == "Следить за жанром":
    bot.send_message(message.chat.id, "Введи название жанра:")
    bot.register_next_step_handler(message, set_genre_tracking)

elif message.text == "Следить за игрой":
    bot.send_message(message.chat.id, "Введи название или ссылку на игру:")
    bot.register_next_step_handler(message, set_game_tracking)

elif message.text == "Назад":
    start_handler(message)
Обзор: сколько всего
def show_sales_overview(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("Подробнее", "Назад")

free_games = get_free_epic_games()
discounted_games = get_discounted_epic_games()

bot.send_message(message.chat.id,
                 f"Сейчас доступно:\n"
                 f"— Бесплатных игр: {len(free_games)}\n"
                 f"— Со скидкой: {len(discounted_games)}",
                 reply_markup=markup)
Подробности: список игр
@bot.message_handler(func=lambda message: message.text == "Подробнее")
def show_detailed_sales(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("Назад")

free_games = get_free_epic_games()
discounted_games = get_discounted_epic_games()

text = "*Бесплатные игры:*\n\n"
for game in free_games:
    text += f"[{game['name']}]({game['link']}) — {game['price']}\n"

text += "\n*Игры со скидкой:*\n\n"
for game in discounted_games:
    text += f"[{game['name']}]({game['link']}) — {game['price']}\n"

bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)
Подписка на жанр
def set_genre_tracking(message):
genre = message.text.lower()
user_genres[message.chat.id] = genre
bot.send_message(message.chat.id, f"Теперь ты следишь за жанром: {genre}!")

Подписка на игру
def set_game_tracking(message):
game = message.text.lower()
user_games[message.chat.id] = game
bot.send_message(message.chat.id, f"Теперь ты следишь за игрой: {game}!")

Запуск
bot.polling(none_stop=True)
