import requests
import vk_api.vk_api
import random
import os
import json
from datetime import datetime as dt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from main.models import CountryStatistics, Regions

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

apiKey = 'd2a2cb674a6cdfa7cf5fbdd8383cc9e6f77694874ed215e806a3b68b751c70bc6ba3dc55ee53f3ce6b801'

countries = {'Мир': 'WORLD', 'Афганистан': 'AF', 'Албания': 'AL', 'Алжир': 'DZ', 'Андорра': 'AD', 'Ангола': 'AO', 'Ангилья': 'AI', 'Антигуа и Барбуда': 'AG', 'Аргентина': 'AR', 'Армения': 'AM', 'Аруба': 'AW', 'Австралия': 'AU', 'Австрия': 'AT', 'Азербайджан': 'AZ', 'Багамы': 'BS', 'Бахрейн': 'BH', 'Бангладеш': 'BD', 'Барбадос': 'BB', 'Беларусь': 'BY', 'Бельгия': 'BE', 'Белиз': 'BZ', 'Бенин': 'BJ', 'Бермуды': 'BM', 'Бутан': 'BT', 'Боливия': 'BO', 'Босния': 'BA', 'Ботсвана': 'BW', 'Бразилия': 'BR', 'Британские Виргинские острова': 'VG', 'Бруней': 'BN', 'Болгария': 'BG', 'Буркина Фасо': 'BF', 'Бурунди': 'BI', 'Кабо-Верде': 'CV', 'Камбоджа': 'KH', 'Камерун': 'CM', 'Канада': 'CA', 'Карибский бассейн Нидерланды': 'BQ', 'Каймановы Острова': 'KY', 'Центрально-Африканская Республика': 'CF', 'Чад': 'TD', 'Нормандские острова': 'JE', 'Чили': 'CL', 'Китай': 'CN', 'Колумбия': 'CO', 'Коморские острова': 'KM', 'Конго': 'CG', 'Коста Рика': 'CR', 'Хорватия': 'HR', 'Куба': 'CU', 'Кюрасао': 'CW', 'Кипр': 'CY', 'Чехия': 'CZ', 'Берег Слоновой Кости': 'CI', 'ДР Конго': 'CD', 'Дания': 'DK', 'Джибути': 'DJ', 'Доминика': 'DM', 'Доминиканская Республика': 'DO', 'Эквадор': 'EC', 'Египет': 'EG', 'Сальвадор': 'SV', 'Экваториальная Гвинея': 'GQ', 'Эритрея': 'ER', 'Эстония': 'EE', 'Эфиопия': 'ET', 'Фолклендские острова': 'FK', 'Фарерские острова': 'FO', 'Фиджи': 'FJ', 'Финляндия': 'FI', 'Франция': 'FR', 'Французская Гвиана': 'GF', 'Французская Полинезия': 'PF', 'Габон': 'GA', 'Гамбия': 'GM', 'Грузия': 'GE', 'Германия': 'DE', 'Гана': 'GH', 'Гибралтар': 'GI', 'Греция': 'GR', 'Гренландия': 'GL', 'Гренада': 'GD', 'Гваделупа': 'GP', 'Гватемала': 'GT', 'Гвинея': 'GN', 'Гвинея-Бисау': 'GW', 'Гайана': 'GY', 'Гаити': 'HT', 'Ватикан': 'VA', 'Гондурас': 'HN', 'Гонконг': 'HK', 'Венгрия': 'HU', 'Исландия': 'IS', 'Индия': 'IN', 'Индонезия': 'ID', 'Иран': 'IR', 'Ирак': 'IQ', 'Ирландия': 'IE', 'Остров Мэн': 'IM', 'Израиль': 'IL', 'Италия': 'IT', 'Ямайка': 'JM', 'Япония': 'JP', 'Иордания': 'JO', 'Казахстан': 'KZ', 'Кения': 'KE', 'Кувейт': 'KW', 'Кыргызстан': 'KG', 'Лаос': 'LA', 'Латвия': 'LV', 'Ливан': 'LB', 'Лесото': 'LS', 'Либерия': 'LR', 'Джамахирия': 'LY', 'Лихтенштейн': 'LI', 'Литва': 'LT', 'Люксембург': 'LU', 'Макао': 'MO', 'Македония': 'MK', 'Мадагаскар': 'MG', 'Малави': 'MW', 'Малайзия': 'MY', 'Мальдивы': 'MV', 'Мали': 'ML', 'Мальта': 'MT', 'Маршалловы острова': 'MH', 'Мартиника': 'MQ', 'Мавритания': 'MR', 'Маврикий': 'MU', 'Майотта': 'YT', 'Мексика': 'MX', 'Микронезия': 'FM', 'Молдова': 'MD', 'Монако': 'MC', 'Монголия': 'MN', 'Монтенегро': 'ME', 'Монтсеррат': 'MS', 'Марокко': 'MA', 'Мозамбик': 'MZ', 'Мьянма': 'MM', 'Намибия': 'NA', 'Непал': 'NP', 'Нидерланды': 'NL', 'Новая Каледония': 'NC', 'Новая Зеландия': 'NZ', 'Никарагуа': 'NI', 'Нигер': 'NE', 'Нигерия': 'NG', 'Норвегия': 'NO', 'Оман': 'OM', 'Пакистан': 'PK', 'Палау': 'PW', 'Палестина': 'PS', 'Панама': 'PA', 'Папуа - Новая Гвинея': 'PG', 'Парагвай': 'PY', 'Перу': 'PE', 'Филиппины': 'PH', 'Польша': 'PL', 'Португалия': 'PT', 'Катар': 'QA', 'Румыния': 'RO', 'Россия': 'RU', 'Руанда': 'RW', 'Реюньон': 'RE', 'Южная Корея': 'KR', 'Остров Св. Елены': 'SH', 'Сент-Китс и Невис': 'KN', 'Санкт-Люсия': 'LC', 'Сен-Мартен': 'MF', 'Сен-Пьер Микелон': 'PM', 'Святой Винсент и Гренадины': 'VC', 'Самоа': 'WS', 'Сан-Марино': 'SM', 'Сан-Томе и Принсипи': 'ST', 'Саудовская Аравия': 'SA', 'Сенегал': 'SN', 'Сербия': 'RS', 'Сейшельские острова': 'SC', 'Сьерра-Леоне': 'SL', 'Сингапур': 'SG', 'Синт-Мартен': 'SX', 'Словакия': 'SK', 'Словения': 'SI', 'Соломоновы острова': 'SB', 'Сомали': 'SO', 'Южная Африка': 'ZA', 'Южный Судан': 'SS', 'Испания': 'ES', 'Шри-Ланка': 'LK', 'Сен-Барт': 'BL', 'Судан': 'SD', 'Суринам': 'SR', 'Свазиленд': 'SZ', 'Швеция': 'SE', 'Швейцария': 'CH', 'Сирия': 'SY', 'Тайвань': 'TW', 'Таджикистан': 'TJ', 'Танзания': 'TZ', 'Таиланд': 'TH', 'Тимор-Лешти': 'TL', 'Того': 'TG', 'Тринидад и Тобаго': 'TT', 'Тунис': 'TN', 'Турция': 'TR', 'Острова Теркс и Кайкос': 'TC', 'ОАЭ': 'AE', 'Великобритания': 'GB', 'США': 'US', 'Уганда': 'UG', 'Украина': 'UA', 'Уругвай': 'UY', 'Узбекистан': 'UZ', 'Вануату': 'VU', 'Венесуэла': 'VE', 'Вьетнам': 'VN', 'Уоллис и Футуна': 'WF', 'Западная Сахара': 'EH', 'Йемен': 'YE', 'Замбия': 'ZM', 'Зимбабве': 'ZW'}
regions = json.loads(Regions.objects.get(id=1).data)
regionskeys = regions.keys()

def command_region(region, *args):
    thisRegion = None
    for i in regionskeys:
        if i.lower().startswith(region.lower()):
            thisRegion = i
            break
    if not thisRegion:
        return f'Регион начинающийся с {region} не был найден. Возможно, вы допустили ошибку в написании.'
    tr = regions[thisRegion]
    return f'''Статистика по региону {thisRegion}
Всего заболевших: {tr['cases']}
Заболевших за сегодня: {tr['cases_delta']}
Смертей: {tr['deaths']}
Смертей за сегодня: {tr['deaths_delta']}

(данные актуальны на момент {tr['date']})
'''

def command_covid(*args):
    if not args:
        country = 'WORLD'
        stats = CountryStatistics.objects.get(country=country)
        datetime = dt.fromtimestamp(int(stats.updated / 1000))
        lastupdatedstring = datetime.strftime('%d.%m.%Y %H:%M:%S')
        return f'''Статистика по миру:
        Больных сейчас: {stats.active}
        Всего заболеваний: {stats.cases}
        Заболеваний сегодня: {stats.todayCases}
        Смертей: {stats.deaths}
        Смертей сегодня: {stats.todayDeaths}
        Выздоровело: {stats.recovered}
        Выздоровело сегодня: {stats.todayRecovered}

        (актуально на момент {lastupdatedstring})
        '''
    else:
        country = None
        countryName = None
        for i in countries.keys():
            if i.lower().startswith(args[0].lower()):
                country = countries[i]
                countryName = i
                break
    if not country:
        return f'Страна начинающаяся с {args[0]} не была найдена. Возможно вы допустили ошибку в написании.'
    stats = CountryStatistics.objects.get(country=country)
    datetime = dt.fromtimestamp(int(stats.updated / 1000))
    lastupdatedstring = datetime.strftime('%d.%m.%Y %H:%M:%S')
    return f'''Статистика по стране {countryName}:
Больных сейчас: {stats.active}
Всего заболеваний: {stats.cases}
Заболеваний сегодня: {stats.todayCases}
Смертей: {stats.deaths}
Смертей сегодня: {stats.todayDeaths}
Выздоровело: {stats.recovered}
Выздоровело сегодня: {stats.todayRecovered}

(актуально на момент {lastupdatedstring})
'''


def command_begin(*args):
    strr = '''Добро пожаловать к боту Ковизавр. У меня вы можете узнать разные вещи о пандемии COVID-19.
Например:
    ''' + command_help()
    return strr


def command_help(*args):
    strr = '''ковид <страна> - выводит статистику о ковиде в указанной стране, например кол-во зараженных
ковид - если не указывать страну, то выводит статистику о ковиде во всем мире
регион <название региона> - выводит статистику о ковиде в указанном регионе России

Не обязательно вводить название региона или страны полностью, можно ввести только первые буквы названия.
'''
    return strr

currentState = {}
COMMANDS = {'ковид': command_covid, 'начать': command_begin, 'помощь': command_help, 'регион': command_region}
SYNTAXES = {'ковид': 'ковид <страна>', 'начать': 'что-то пошло не так', 'помощь': 'что-то пошло не так', 'регион': 'регион <название региона>'}

def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])

class Server:
    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        # Даем серверу имя
        print(api_token)
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        self.vk_api.messages.send(peer_id=send_id,
                                  message=message,
                                  random_id=get_random_id())

    def test(self):
        # Посылаем сообщение пользователю с указанным ID
        self.send_msg(230112961, "Привет-привет!")

    def start(self):
        for event in self.long_poll.listen():
            print(event)
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.object.message['text'].lower().split()
                id = event.object.message['peer_id']
                if msg[0] not in COMMANDS:
                    print(id)
                    self.send_msg(id, 'Неизвестная команда, список команд доступен если написать \'помощь\'')
                else:
                    try:
                        self.send_msg(id, COMMANDS[msg[0]](*msg[1:]))
                    except TypeError:
                        self.send_msg(id, 'Неправильно введена команда. Синтаксис команды: ' + SYNTAXES[msg[0]])



vk = Server(apiKey, 207931688)
vk.start()