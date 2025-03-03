import telebot
from telebot import types
import requests
import wikipedia
from bs4 import BeautifulSoup

# API токен бота
API_TOKEN = '7697130153:AAHjrKm4FVmBEGTxZcanyJpRz-UdHc5x8lA'
bot = telebot.TeleBot(API_TOKEN)

# Список жанров
genres = [
    "Action", "Adventure", "RPG", "Strategy", "Simulation",
    "Racing", "Sports", "Puzzle", "Horror", "Multiplayer",
    "Shooter", "Platformer", "Fighting", "Survival", "Open World",
    "Stealth", "Battle Royale", "MMORPG", "Sandbox", "Indie",
    "Casual", "Party", "Educational", "VR", "Card Game",
    "Turn-Based", "Real-Time", "Tactical", "Roguelike", "Metroidvania"
]

# Данные по играм
games_data = {
    "free": [],
    "discounted": []
}

# Кэш для хранения жанров игр
genre_cache = {}

def get_genres_from_wikipedia(game_title):
    """Получает жанры игры из Wikipedia"""
    try:
        # Ищем статью по названию игры
        page = wikipedia.page(game_title)
        # Получаем текст статьи
        text = page.content
        # Ищем жанры в тексте статьи
        found_genres = [genre for genre in genres if genre.lower() in text.lower()]
        return found_genres
    except wikipedia.exceptions.PageError:
        # Если статья не найдена
        return []
    except wikipedia.exceptions.DisambiguationError:
        # Если запрос неоднозначен (например, "Mario" может быть и игрой, и персонажем)
        return []

def get_genres_from_fandom(game_title):
    """Получает жанры из Fandom (если найдётся статья)"""
    search_url = f"https://www.fandom.com/?s={game_title.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_result = soup.find("a", {"class": "search-result__title"})
        
        if first_result:
            game_url = first_result["href"]
            game_page = requests.get(game_url, headers=headers)
            game_soup = BeautifulSoup(game_page.text, 'html.parser')
            
            genre_section = game_soup.find("div", {"data-source": "genre"})
            if genre_section:
                return [genre.text.strip() for genre in genre_section.find_all("a")]
    
    return []

def get_game_genres(game_title):
    """Получает жанры игры, используя несколько источников"""
    # Проверяем кэш
    if game_title in genre_cache:
        return genre_cache[game_title]
    
    # Получаем жанры из Wikipedia
    genres = get_genres_from_wikipedia(game_title)
    
    # Если жанры не найдены, пробуем Fandom
    if not genres:
        genres = get_genres_from_fandom(game_title)
    
    # Кэшируем результат
    genre_cache[game_title] = genres
    
    return genres

def parse_epic_games():
    """Парсит бесплатные и скидочные игры из Epic Games Store"""
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
    response = requests.get(url)
    data = response.json()

    games_data["free"].clear()
    games_data["discounted"].clear()

    if 'data' in data and 'Catalog' in data['data']:
        for game in data['data']['Catalog']['searchStore']['elements']:
            title = game.get('title', 'Нет названия')
            price_info = game.get('price', {}).get('totalPrice', {}).get('fmtPrice', {})
            original_price = price_info.get('originalPrice', 'Нет цены')
            discount_price = price_info.get('discountPrice', '0.00')
            is_free = discount_price == "0" or discount_price == "0.00"

            # Получаем жанры
            game_genres = get_game_genres(title)

            game_info = {
                "title": title,
                "price": original_price,
                "discount": discount_price,
                "is_free": is_free,
                "genres": game_genres
            }

            if is_free:
                games_data["free"].append(game_info)
            else:
                games_data["discounted"].append(game_info)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Игры на распродаже")
    btn2 = types.KeyboardButton("Следить за жанром")
    btn3 = types.KeyboardButton("Следить за игрой")
    markup.add(btn1, btn2, btn3)

    bot.reply_to(message, "Привет! Я бот для Epic Games Store. Что ты хочешь сделать?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Следить за жанром")
def ask_for_genre(message):
    """Запрашивает у пользователя жанр для отслеживания"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(genre) for genre in genres]
    markup.add(*buttons)
    markup.add(types.KeyboardButton("Назад"))
    bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in genres)
def show_games_by_genre(message):
    """Показывает игры определенного жанра"""
    genre = message.text
    found_games = [game for game in games_data["free"] + games_data["discounted"] if genre in game['genres']]

    if found_games:
        response = f"🎮 Найдены игры в жанре '{genre}':\n"
        for game in found_games:
            response += f"- {game['title']} ({game['price']})\n"
    else:
        response = f"Игр в жанре '{genre}' не найдено."

    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: message.text == "Назад")
def go_back(message):
    """Возвращает пользователя в главное меню"""
    send_welcome(message)

# Запуск бота
bot.polling(none_stop=True)
