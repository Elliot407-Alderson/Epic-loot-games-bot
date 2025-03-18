import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from difflib import get_close_matches

TOKEN = "7665106663:AAGsk4vfin0EPw7n-kZqNabUhHPQ17smUHM"
bot = telebot.TeleBot(TOKEN)

# База данных (первые 3 игры)
games = [
    {"title": "Hollow Knight", "genre": "Метроидвания", "platform": "PC, Switch, PS4", "rating": 9.3, "link": "https://www.teamcherry.com.au/hollowknight"},
    {"title": "Celeste", "genre": "Платформер", "platform": "PC, Switch, PS4, Xbox", "rating": 9.5, "link": "https://mattmakesgames.com"},
    {"title": "Hades", "genre": "Рогалик, Экшен", "platform": "PC, Switch, PS4, PS5, Xbox", "rating": 9.6, "link": "https://www.supergiantgames.com/games/hades"},
    {"title": "Stray", "genre": "Приключенческая игра", "platform": "PC, PS4, PS5", "rating": 9.0, "link": "https://ru.wikipedia.org/wiki/Stray_(игра)"},
    {"title": "Sable", "genre": "Приключенческая игра", "platform": "PC, Xbox One, Xbox Series X/S", "rating": 8.5, "link": "https://ru.wikipedia.org/wiki/Sable"},
    {"title": "Limbo", "genre": "Платформер, Головоломка", "platform": "PC, PS3, PS4, PS5, Xbox 360, Xbox One, Xbox Series X/S, Switch, iOS", "rating": 9.0, "link": "https://ru.wikipedia.org/wiki/Limbo_(игра)"},
    {"title": "Cuphead", "genre": "Платформер, Шутер", "platform": "PC, PS4, PS5, Xbox One, Xbox Series X/S, Switch", "rating": 9.0, "link": "https://cupheadgame.com/"},
    {"title": "Undertale", "genre": "РПГ", "platform": "PC, PS4, PS5, Switch, Xbox", "rating": 9.7, "link": "https://undertale.com/"},
    {"title": "Inside", "genre": "Платформер, Головоломка", "platform": "PC, PS4, PS5, Xbox One, Xbox Series X/S, Switch, iOS", "rating": 9.2, "link": "https://playdead.com/games/inside/"},
    {"title": "Stardew Valley", "genre": "Симулятор, РПГ", "platform": "PC, PS4, PS5, Switch, Xbox, Mobile", "rating": 9.6, "link": "https://www.stardewvalley.net/"},
    {"title": "The Messenger", "genre": "Платформер, Метроидвания", "platform": "PC, Switch, PS4, Xbox One", "rating": 8.8, "link": "https://themessengergame.com/"},
    {"title": "Katana ZERO", "genre": "Экшен, Платформер", "platform": "PC, Switch, Xbox One", "rating": 9.1, "link": "https://www.askiisoft.com/games/katana-zero/"},
    {"title": "Dead Cells", "genre": "Рогалик, Метроидвания", "platform": "PC, PS4, PS5, Switch, Xbox, Mobile", "rating": 9.3, "link": "https://dead-cells.com/"},
    {"title": "Hyper Light Drifter", "genre": "Экшен, РПГ", "platform": "PC, PS4, PS5, Switch, Xbox", "rating": 9.0, "link": "https://heart-machine.com/"},
    {"title": "Oxenfree", "genre": "Приключение, Хоррор", "platform": "PC, PS4, PS5, Switch, Xbox, Mobile", "rating": 8.7, "link": "https://www.nightschoolstudio.com/oxenfree/"},
    {"title": "Slay the Spire", "genre": "Рогалик, Карточная игра", "platform": "PC, PS4, PS5, Switch, Xbox, Mobile", "rating": 9.4, "link": "https://www.megacrit.com/"},
    {"title": "Bastion", "genre": "Экшен, РПГ", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 9.0, "link": "https://www.supergiantgames.com/games/bastion/"},
    {"title": "Transistor", "genre": "Экшен, РПГ", "platform": "PC, PS4, Switch", "rating": 9.1, "link": "https://www.supergiantgames.com/games/transistor/"},
    {"title": "Disco Elysium", "genre": "РПГ, Детектив", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.7, "link": "https://zaumstudio.com/"},
    {"title": "Return of the Obra Dinn", "genre": "Детектив, Головоломка", "platform": "PC, PS4, Xbox, Switch", "rating": 9.4, "link": "https://obradinn.com/"},
    {"title": "Outer Wilds", "genre": "Приключенческая игра, Головоломка", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.6, "link": "https://www.mobiusdigitalgames.com/"},
    {"title": "Firewatch", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://www.firewatchgame.com/"},
    {"title": "What Remains of Edith Finch", "genre": "Приключенческая игра", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.2, "link": "https://www.giantsparrow.com/games/finch/"},
    {"title": "Gris", "genre": "Платформер, Приключенческая игра", "platform": "PC, PS4, Switch, Mobile", "rating": 9.0, "link": "https://nomada.studio/gris/"},
    {"title": "Ori and the Blind Forest", "genre": "Платформер, Метроидвания", "platform": "PC, Xbox, Switch", "rating": 9.3, "link": "https://www.orithegame.com/blind-forest/"},
    {"title": "Ori and the Will of the Wisps", "genre": "Платформер, Метроидвания", "platform": "PC, Xbox, Switch", "rating": 9.5, "link": "https://www.orithegame.com/will-of-the-wisps/"},
    {"title": "A Short Hike", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 9.1, "link": "https://ashorthike.com/"},
    {"title": "Spiritfarer", "genre": "Симулятор, Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://www.spiritfarer.com/"},
    {"title": "Tunic", "genre": "Экшен, Приключенческая игра", "platform": "PC, Xbox, Switch", "rating": 9.2, "link": "https://tunicgame.com/"},
    {"title": "Eastward", "genre": "РПГ, Приключенческая игра", "platform": "PC, Switch", "rating": 8.9, "link": "https://www.eastwardgame.com/"},
    {"title": "Night in the Woods", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://www.nightinthewoods.com/"},
    {"title": "Subnautica", "genre": "Приключенческая игра, Выживание", "platform": "PC, PS4, Xbox, Switch", "rating": 9.3, "link": "https://unknownworlds.com/subnautica/"},
    {"title": "The Witness", "genre": "Головоломка", "platform": "PC, PS4, Xbox, Mobile", "rating": 9.2, "link": "https://the-witness.net/"},
    {"title": "Braid", "genre": "Платформер, Головоломка", "platform": "PC, PS3, PS4, Xbox, Switch", "rating": 9.0, "link": "https://braid-game.com/"},
    {"title": "Fez", "genre": "Платформер, Головоломка", "platform": "PC, PS4, Xbox, Switch", "rating": 9.1, "link": "https://fezgame.com/"},
    {"title": "The Stanley Parable", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://www.stanleyparable.com/"},
    {"title": "Papers, Please", "genre": "Симулятор, Головоломка", "platform": "PC, PS Vita, iOS", "rating": 9.2, "link": "https://papersplea.se/"},
    {"title": "Her Story", "genre": "Детектив, Интерактивное кино", "platform": "PC, iOS", "rating": 8.8, "link": "https://www.herstorygame.com/"},
    {"title": "The Binding of Isaac", "genre": "Рогалик, Экшен", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 9.1, "link": "https://bindingofisaac.com/"},
    {"title": "Darkest Dungeon", "genre": "РПГ, Рогалик", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 9.0, "link": "https://www.darkestdungeon.com/"},
    {"title": "Baba Is You", "genre": "Головоломка", "platform": "PC, Switch, Mobile", "rating": 9.2, "link": "https://www.hempuli.com/baba/"},
    {"title": "Into the Breach", "genre": "Стратегия", "platform": "PC, Switch, Mobile", "rating": 9.1, "link": "https://subsetgames.com/itb.html"},
    {"title": "FTL: Faster Than Light", "genre": "Стратегия, Рогалик", "platform": "PC, iOS", "rating": 9.0, "link": "https://subsetgames.com/ftl.html"},
    {"title": "Don't Starve", "genre": "Выживание", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 8.9, "link": "https://www.klei.com/games/dont-starve"},
    {"title": "Risk of Rain 2", "genre": "Рогалик, Экшен", "platform": "PC, PS4, Xbox, Switch", "rating": 9.1, "link": "https://hopoo.tumblr.com/"},
    {"title": "Hollow Knight: Gods & Nightmares", "genre": "Метроидвания", "platform": "PC, Switch, PS4", "rating": 9.3, "link": "https://www.teamcherry.com.au/hollowknight"},
    {"title": "Axiom Verge", "genre": "Метроидвания", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://www.axiomverge.com/"},
    {"title": "Axiom Verge 2", "genre": "Метроидвания", "platform": "PC, PS4, PS5, Switch", "rating": 8.7, "link": "https://www.axiomverge2.com/"},
    {"title": "Blasphemous", "genre": "Метроидвания, Платформер", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://blasphemousgame.com/"},
    {"title": "Carrion", "genre": "Экшен, Хоррор", "platform": "PC, PS4, Xbox, Switch", "rating": 8.5, "link": "https://carriongame.com/"},
    {"title": "Children of Morta", "genre": "Рогалик, РПГ", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://www.childrenofmorta.com/"},
    {"title": "CrossCode", "genre": "РПГ, Экшен", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://www.cross-code.com/"},
    {"title": "Darkwood", "genre": "Хоррор, Выживание", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://darkwoodgame.com/"},
    {"title": "Dead Estate", "genre": "Рогалик, Шутер", "platform": "PC", "rating": 8.6, "link": "https://store.steampowered.com/app/1207400/Dead_Estate/"},
    {"title": "Dicey Dungeons", "genre": "Рогалик, Карточная игра", "platform": "PC, Switch, Mobile", "rating": 8.7, "link": "https://diceydungeons.com/"},
    {"title": "Dusk", "genre": "Шутер", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://dusk.fyi/"},
    {"title": "Enderal: Forgotten Stories", "genre": "РПГ", "platform": "PC", "rating": 9.3, "link": "https://sureai.net/games/enderal/"},
    {"title": "Enter the Gungeon", "genre": "Рогалик, Шутер", "platform": "PC, PS4, Xbox, Switch", "rating": 9.1, "link": "https://dodgeroll.com/gungeon/"},
    {"title": "Everhood", "genre": "Ритм-игра, Приключенческая игра", "platform": "PC, Switch", "rating": 8.8, "link": "https://everhoodgame.com/"},
    {"title": "Furi", "genre": "Экшен, Босс-раш", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://thegamebakers.com/games/furi/"},
    {"title": "Gorogoa", "genre": "Головоломка", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 9.0, "link": "https://gorogoa.com/"},
    {"title": "Hob", "genre": "Приключенческая игра", "platform": "PC, PS4, Switch", "rating": 8.7, "link": "https://www.hobgame.com/"},
    {"title": "Iconoclasts", "genre": "Платформер, Метроидвания", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://www.iconoclastsgame.com/"},
    {"title": "Inscryption", "genre": "Карточная игра, Хоррор", "platform": "PC, PS4, PS5, Switch", "rating": 9.4, "link": "https://www.inscryption.com/"},
    {"title": "Journey", "genre": "Приключенческая игра", "platform": "PC, PS4, iOS", "rating": 9.2, "link": "https://thatgamecompany.com/journey/"},
    {"title": "Kentucky Route Zero", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://kentuckyroutezero.com/"},
    {"title": "Little Nightmares", "genre": "Хоррор, Платформер", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://www.bandainamcoent.com/games/little-nightmares"},
    {"title": "Little Nightmares II", "genre": "Хоррор, Платформер", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.0, "link": "https://www.bandainamcoent.com/games/little-nightmares-ii"},
    {"title": "Moonlighter", "genre": "РПГ, Симулятор", "platform": "PC, PS4, Xbox, Switch", "rating": 8.6, "link": "https://www.moonlightergame.com/"},
    {"title": "Noita", "genre": "Рогалик, Экшен", "platform": "PC, Switch", "rating": 8.9, "link": "https://noitagame.com/"},
    {"title": "Oxygen Not Included", "genre": "Симулятор, Выживание", "platform": "PC, PS4, Xbox, Switch", "rating": 9.0, "link": "https://www.klei.com/games/oxygen-not-included"},
    {"title": "Pathologic 2", "genre": "РПГ, Хоррор", "platform": "PC, PS4, Xbox", "rating": 8.7, "link": "https://pathologic2.com/"},
    {"title": "Rain World", "genre": "Платформер, Выживание", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://rainworldgame.com/"},
    {"title": "Rogue Legacy 2", "genre": "Рогалик, Платформер", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.1, "link": "https://www.roguelegacy2.com/"},
    {"title": "Sayonara Wild Hearts", "genre": "Ритм-игра, Аркада", "platform": "PC, PS4, Xbox, Switch, iOS", "rating": 8.9, "link": "https://www.sayonarawildhearts.com/"},
    {"title": "The Artful Escape", "genre": "Приключенческая игра", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 8.7, "link": "https://www.theartfulescape.com/"},
    {"title": "The Long Dark", "genre": "Выживание", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://www.thelongdark.com/"},
    {"title": "The Red Strings Club", "genre": "Приключенческая игра", "platform": "PC, Switch", "rating": 8.8, "link": "https://www.theredstringsclub.com/"},
    {"title": "The Swapper", "genre": "Платформер, Головоломка", "platform": "PC, PS4, Xbox, Switch", "rating": 8.9, "link": "https://www.facepalmgames.com/the-swapper/"},
    {"title": "Thumper", "genre": "Ритм-игра", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://www.thumpergame.com/"},
    {"title": "To the Moon", "genre": "Приключенческая игра", "platform": "PC, PS4, Xbox, Switch, Mobile", "rating": 9.0, "link": "https://freebirdgames.com/to-the-moon/"},
    {"title": "Undermine", "genre": "Рогалик, Экшен", "platform": "PC, PS4, Xbox, Switch", "rating": 8.7, "link": "https://www.underminegame.com/"},
    {"title": "Valheim", "genre": "Выживание, Экшен", "platform": "PC", "rating": 9.3, "link": "https://www.valheimgame.com/"},
    {"title": "Wargroove", "genre": "Стратегия", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://wargroove.com/"},
    {"title": "Wizard of Legend", "genre": "Рогалик, Экшен", "platform": "PC, PS4, Xbox, Switch", "rating": 8.7, "link": "https://www.wizardoflegend.com/"},
    {"title": "Yoku's Island Express", "genre": "Платформер, Пинбол", "platform": "PC, PS4, Xbox, Switch", "rating": 8.8, "link": "https://www.yokuislandexpress.com/"},
    {"title": "Hades II", "genre": "Рогалик, Экшен", "platform": "PC", "rating": 9.5, "link": "https://www.supergiantgames.com/games/hades-ii"},
    {"title": "Cocoon", "genre": "Головоломка, Приключенческая игра", "platform": "PC, Xbox, Switch", "rating": 9.0, "link": "https://www.cocoongame.com/"},
    {"title": "Sea of Stars", "genre": "РПГ, Приключенческая игра", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 9.2, "link": "https://www.seaofstarsgame.com/"},
    {"title": "Viewfinder", "genre": "Головоломка, Приключенческая игра", "platform": "PC, PS4, PS5", "rating": 8.9, "link": "https://www.viewfindergame.com/"},
    {"title": "Dredge", "genre": "Приключенческая игра, Хоррор", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 8.8, "link": "https://www.dredgegame.com/"},
    {"title": "Chants of Sennaar", "genre": "Головоломка, Приключенческая игра", "platform": "PC, PS4, Xbox, Switch", "rating": 8.7, "link": "https://www.chantsofsennaar.com/"},
    {"title": "Planet of Lana", "genre": "Приключенческая игра, Платформер", "platform": "PC, Xbox", "rating": 8.6, "link": "https://www.planetoflana.com/"},
    {"title": "The Last Case of Benedict Fox", "genre": "Метроидвания, Хоррор", "platform": "PC, Xbox", "rating": 8.5, "link": "https://www.benedictfoxgame.com/"},
    {"title": "Venba", "genre": "Приключенческая игра, Визуальная новелла", "platform": "PC, Xbox, Switch", "rating": 8.7, "link": "https://www.venbagame.com/"},
    {"title": "Lies of P", "genre": "Экшен, РПГ", "platform": "PC, PS4, PS5, Xbox", "rating": 9.1, "link": "https://www.liesofp.com/"},
    {"title": "Hollow Knight: Silksong", "genre": "Метроидвания", "platform": "PC, Switch", "rating": 9.4, "link": "https://www.teamcherry.com.au/silksong"},
    {"title": "Tchia", "genre": "Приключенческая игра", "platform": "PC, PS4, PS5", "rating": 8.8, "link": "https://www.tchiagame.com/"},
    {"title": "The Cosmic Wheel Sisterhood", "genre": "Визуальная новелла, Головоломка", "platform": "PC, Switch", "rating": 8.7, "link": "https://www.cosmicwheelsisterhood.com/"},
    {"title": "Saltsea Chronicles", "genre": "Приключенческая игра", "platform": "PC, PS5, Switch", "rating": 8.6, "link": "https://www.saltseachronicles.com/"},
    {"title": "Naiad", "genre": "Приключенческая игра", "platform": "PC", "rating": 8.5, "link": "https://www.naiadgame.com/"},
    {"title": "The Plucky Squire", "genre": "Приключенческая игра, Платформер", "platform": "PC, PS5, Xbox, Switch", "rating": 8.9, "link": "https://www.thepluckysquire.com/"},
    {"title": "Replaced", "genre": "Экшен, Платформер", "platform": "PC, Xbox", "rating": 8.7, "link": "https://www.replacedgame.com/"},
    {"title": "Nightingale", "genre": "Выживание, Приключенческая игра", "platform": "PC", "rating": 8.8, "link": "https://www.nightingalegame.com/"},
    {"title": "Sable: The Forgotten Shards", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.6, "link": "https://www.sablegame.com/forgotten-shards"},
    {"title": "The Wandering Village", "genre": "Симулятор, Стратегия", "platform": "PC", "rating": 8.7, "link": "https://www.thewanderingvillage.com/"},
    {"title": "Kena: Bridge of Spirits", "genre": "Приключенческая игра, Экшен", "platform": "PC, PS4, PS5", "rating": 8.9, "link": "https://www.emberlab.com/kena/"},
    {"title": "Solar Ash", "genre": "Экшен, Платформер", "platform": "PC, PS4, PS5", "rating": 8.7, "link": "https://www.solarashgame.com/"},
    {"title": "Sable", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.5, "link": "https://www.shedworks.co.uk/sable"},
    {"title": "The Artful Escape", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.6, "link": "https://www.theartfulescape.com/"},
    {"title": "The Forgotten City", "genre": "Приключенческая игра, Детектив", "platform": "PC, PS4, PS5, Xbox, Switch", "rating": 8.8, "link": "https://www.forgottencitygame.com/"},
    {"title": "The Ascent", "genre": "Экшен, РПГ", "platform": "PC, Xbox", "rating": 8.7, "link": "https://www.theascentgame.com/"},
    {"title": "Chicory: A Colorful Tale", "genre": "Приключенческая игра, Головоломка", "platform": "PC, PS4, PS5, Switch", "rating": 8.9, "link": "https://www.chicorygame.com/"},
    {"title": "Loop Hero", "genre": "Рогалик, Стратегия", "platform": "PC, Switch", "rating": 8.8, "link": "https://www.loophero.com/"},
    {"title": "Unsighted", "genre": "Экшен, Метроидвания", "platform": "PC, PS4, Xbox, Switch", "rating": 8.7, "link": "https://www.unsightedgame.com/"},
    {"title": "Eastward", "genre": "РПГ, Приключенческая игра", "platform": "PC, Switch", "rating": 8.9, "link": "https://www.eastwardgame.com/"},
    {"title": "Omno", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.6, "link": "https://www.omnogame.com/"},
    {"title": "The Wild at Heart", "genre": "Приключенческая игра, Головоломка", "platform": "PC, Xbox, Switch", "rating": 8.5, "link": "https://www.thewildatheartgame.com/"},
    {"title": "Lake", "genre": "Приключенческая игра, Симулятор", "platform": "PC, Xbox", "rating": 8.4, "link": "https://www.lakegame.com/"},
    {"title": "Road 96", "genre": "Приключенческая игра", "platform": "PC, Switch", "rating": 8.7, "link": "https://www.road96game.com/"},
    {"title": "The Gunk", "genre": "Приключенческая игра, Экшен", "platform": "PC, Xbox", "rating": 8.3, "link": "https://www.thegunkgame.com/"},
    {"title": "Echo Generation", "genre": "РПГ, Приключенческая игра", "platform": "PC, Xbox", "rating": 8.5, "link": "https://www.echogeneration.com/"},
    {"title": "Sable: The Forgotten Shards", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.6, "link": "https://www.sablegame.com/forgotten-shards"},
    {"title": "The Big Con", "genre": "Приключенческая игра", "platform": "PC, Xbox", "rating": 8.4, "link": "https://www.thebigcongame.com/"},
    {"title": "Beacon Pines", "genre": "Приключенческая игра, Визуальная новелла", "platform": "PC, Xbox, Switch", "rating": 8.7, "link": "https://www.beaconpines.com/"},
    {"title": "Tunic", "genre": "Экшен, Приключенческая игра", "platform": "PC, Xbox, Switch", "rating": 9.0, "link": "https://www.tunicgame.com/"}
]
# Списки пользователей
user_lists = {}  # {chat_id: {"want_to_play": set(), "completed": set()}}

# Уникальные жанры и платформы
genres = sorted(set(g for game in games for g in game["genre"].split(", ")))
platforms = sorted(set(p for game in games for p in game["platform"].split(", ")))

# Улучшенная система исправления опечаток
def correct_typo(user_input, games_list):
    game_titles = [game["title"].lower() for game in games_list]
    matches = get_close_matches(user_input.lower(), game_titles, n=1, cutoff=0.4)  # Порог схожести 40%
    if matches:
        corrected_title = matches[0]
        for game in games_list:
            if game["title"].lower() == corrected_title:
                return game["title"]
    return None

# Функция для добавления игры в список
def add_to_list(chat_id, game_title, list_name):
    # Инициализируем списки, если их нет
    if chat_id not in user_lists:
        user_lists[chat_id] = {"want_to_play": set(), "completed": set()}
    
    # Добавляем игру в выбранный список
    user_lists[chat_id][list_name].add(game_title)

# Функция для удаления игры из списка
def remove_from_list(chat_id, game_title, list_name):
    if chat_id in user_lists and game_title in user_lists[chat_id][list_name]:
        user_lists[chat_id][list_name].remove(game_title)
        return True
    return False

# Функция для получения топа игр (исключая игры из списков)
def get_top_games(chat_id, limit=5):
    excluded_games = user_lists.get(chat_id, {}).get("want_to_play", set()).union(
        user_lists.get(chat_id, {}).get("completed", set()))
    sorted_games = sorted([g for g in games if g["title"] not in excluded_games], key=lambda x: x["rating"], reverse=True)
    return sorted_games[:limit]

# Функция для поиска игр по жанру и платформе
def find_games_by_genre_and_platform(genre, platform, excluded_games):
    return [
        g for g in games
        if genre.lower() in g["genre"].lower() and platform.lower() in g["platform"].lower() and g["title"] not in excluded_games
    ]

# Создание Inline-клавиатуры
def create_inline_keyboard(buttons, row_width=2):
    markup = InlineKeyboardMarkup(row_width=row_width)
    for button in buttons:
        if isinstance(button, tuple):  # Если кнопка с callback_data
            markup.add(InlineKeyboardButton(button[0], callback_data=button[1]))
        else:  # Если просто текст
            markup.add(InlineKeyboardButton(button, callback_data=button))
    return markup

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    markup = create_inline_keyboard([
        ("Поиск по жанру и платформе", "search_genre_platform"),
        ("Топ игр по рейтингу", "top_games"),
        ("Мои списки", "my_lists"),
        ("Пополнить списки", "add_games")
    ])
    bot.send_message(chat_id, "Привет! Я помогу тебе найти крутые инди-игры. Выбери действие:", reply_markup=markup)

# Обработчик inline-кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    chat_id = call.message.chat.id
    data = call.data

    if data == "search_genre_platform":
        markup = create_inline_keyboard([(genre, f"genre_{genre}") for genre in genres])
        bot.send_message(chat_id, "Выбери жанр:", reply_markup=markup)
    elif data == "top_games":
        top_games = get_top_games(chat_id, limit=5)
        if top_games:
            text = "\n\n".join([f"🎮 {g['title']} ({g['rating']}/10)\n🔗 {g['link']}" for g in top_games])
            markup = create_inline_keyboard([("Главное меню", "main_menu")])
            bot.send_message(chat_id, f"Топ игр по рейтингу:\n{text}", reply_markup=markup, disable_web_page_preview=True)
        else:
            bot.send_message(chat_id, "Нет игр для рекомендаций. Добавь игры в списки 'Хочу пройти' или 'Прошел'.")
    elif data == "my_lists":
        show_my_lists(call)
    elif data == "add_games":
        bot.send_message(chat_id, "Введи название игры:")
    elif data.startswith("genre_"):
        genre = data.split("_", 1)[1]
        user_lists[chat_id] = user_lists.get(chat_id, {"selected_genre": None})
        user_lists[chat_id]["selected_genre"] = genre
        markup = create_inline_keyboard([(platform, f"platform_{platform}") for platform in platforms])
        bot.send_message(chat_id, f"Выбран жанр: {genre}. Теперь выбери платформу:", reply_markup=markup)
    elif data.startswith("platform_"):
        platform = data.split("_", 1)[1]
        selected_genre = user_lists.get(chat_id, {}).get("selected_genre")
        if not selected_genre:
            bot.send_message(chat_id, "Сначала выбери жанр.")
            return

        excluded_games = user_lists.get(chat_id, {}).get("want_to_play", set()).union(
            user_lists.get(chat_id, {}).get("completed", set()))
        found_games = find_games_by_genre_and_platform(selected_genre, platform, excluded_games)

        if found_games:
            text = "\n\n".join([f"🎮 {g['title']} ({g['rating']}/10)\nЖанр: {g['genre']}\n🔗 {g['link']}" for g in found_games])
            markup = create_inline_keyboard([("Главное меню", "main_menu")])
            bot.send_message(chat_id, f"Найденные игры:\n{text}", reply_markup=markup, disable_web_page_preview=True)
        else:
            bot.send_message(chat_id, "Игры по запросу не найдены.")
    elif data == "main_menu":
        start(call.message)
    elif data.startswith("want_") or data.startswith("completed_"):
        handle_list_buttons(call)

# Обработчик кнопки "Мои списки"
# Обработчик кнопки "Мои списки"
def show_my_lists(call):
    chat_id = call.message.chat.id

    # Проверяем, есть ли у пользователя списки
    if chat_id in user_lists and (user_lists[chat_id]["want_to_play"] or user_lists[chat_id]["completed"]):
        # Если есть, показываем оба списка
        want_to_play = user_lists[chat_id]["want_to_play"]
        completed = user_lists[chat_id]["completed"]

        # Формируем текст для списка "Хочу пройти"
        if want_to_play:
            want_to_play_text = "🎮 Список 'Хочу пройти':\n"
            want_to_play_text += "\n".join([f"- {game}" for game in want_to_play])
        else:
            want_to_play_text = "🎮 Список 'Хочу пройти' пуст."

        # Формируем текст для списка "Прошел"
        if completed:
            completed_text = "🎮 Список 'Прошел':\n"
            completed_text += "\n".join([f"- {game}" for game in completed])
        else:
            completed_text = "🎮 Список 'Прошел' пуст."

        # Объединяем тексты
        final_text = f"{want_to_play_text}\n\n{completed_text}"

        # Создаем клавиатуру только с кнопкой "Главное меню"
        markup = create_inline_keyboard([("Главное меню", "main_menu")])
        bot.send_message(chat_id, final_text, reply_markup=markup)
    else:
        # Если списков нет, показываем сообщение и кнопку "Главное меню"
        markup = create_inline_keyboard([("Главное меню", "main_menu")])
        bot.send_message(chat_id, "У тебя пока нет списков игр.", reply_markup=markup)
# Обработчик текстовых сообщений (для добавления игры)
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    user_input = message.text.strip()

    # Исправление опечаток
    corrected_title = correct_typo(user_input, games)
    if corrected_title:
        # Показываем информацию об игре
        game_info = next(g for g in games if g["title"] == corrected_title)
        text = f"🎮 {game_info['title']}\nЖанр: {game_info['genre']}\nПлатформа: {game_info['platform']}\nРейтинг: {game_info['rating']}/10\n🔗 {game_info['link']}"

        # Кнопки для добавления в списки
        markup = create_inline_keyboard([
            ("Хочу пройти", f"want_{corrected_title}"),
            ("Прошел", f"completed_{corrected_title}")
        ])
        bot.send_message(chat_id, f"Возможно, вы имели в виду:\n{text}", reply_markup=markup, disable_web_page_preview=True)
    else:
        bot.send_message(chat_id, "Игра не найдена. Попробуй еще раз.")

# Обработчик кнопок "Хочу пройти" и "Прошел"
@bot.callback_query_handler(func=lambda call: call.data.startswith(("want_", "completed_")))
def handle_list_buttons(call):
    chat_id = call.message.chat.id
    action, game_title = call.data.split("_", 1)

    # Проверяем, существует ли игра в базе данных
    if not any(game["title"] == game_title for game in games):
        bot.send_message(chat_id, "Игра не найдена в базе данных.")
        return

    if action == "want":
        add_to_list(chat_id, game_title, "want_to_play")
        bot.send_message(chat_id, f"Игра {game_title} добавлена в список 'Хочу пройти'.")
    elif action == "completed":
        add_to_list(chat_id, game_title, "completed")
        bot.send_message(chat_id, f"Игра {game_title} добавлена в список 'Прошел'.")

    # Удаляем кнопки из сообщения
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)

# Запуск бота
bot.polling()
