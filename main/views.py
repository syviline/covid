from django.shortcuts import render, redirect
from .models import CountryStatistics, ipCountries, HistoricData
import requests
from datetime import datetime as dt


countries = {
'WORLD': 'Мир',
'AF': 'Афганистан',
'AL': 'Албания',
'DZ': 'Алжир',
'AD': 'Андорра',
'AO': 'Ангола',
'AI': 'Ангилья',
'AG': 'Антигуа и Барбуда',
'AR': 'Аргентина',
'AM': 'Армения',
'AW': 'Аруба',
'AU': 'Австралия',
'AT': 'Австрия',
'AZ': 'Азербайджан',
'BS': 'Багамы',
'BH': 'Бахрейн',
'BD': 'Бангладеш',
'BB': 'Барбадос',
'BY': 'Беларусь',
'BE': 'Бельгия',
'BZ': 'Белиз',
'BJ': 'Бенин',
'BM': 'Бермуды',
'BT': 'Бутан',
'BO': 'Боливия',
'BA': 'Босния',
'BW': 'Ботсвана',
'BR': 'Бразилия',
'VG': 'Британские Виргинские острова',
'BN': 'Бруней',
'BG': 'Болгария',
'BF': 'Буркина Фасо',
'BI': 'Бурунди',
'CV': 'Кабо-Верде',
'KH': 'Камбоджа',
'CM': 'Камерун',
'CA': 'Канада',
'BQ': 'Карибский бассейн Нидерланды',
'KY': 'Каймановы Острова',
'CF': 'Центрально-Африканская Республика',
'TD': 'Чад',
'JE': 'Нормандские острова',
'CL': 'Чили',
'CN': 'Китай',
'CO': 'Колумбия',
'KM': 'Коморские острова',
'CG': 'Конго',
'CR': 'Коста Рика',
'HR': 'Хорватия',
'CU': 'Куба',
'CW': 'Кюрасао',
'CY': 'Кипр',
'CZ': 'Чехия',
'CI': 'Берег Слоновой Кости',
'CD': 'ДР Конго',
'DK': 'Дания',
'DJ': 'Джибути',
'DM': 'Доминика',
'DO': 'Доминиканская Республика',
'EC': 'Эквадор',
'EG': 'Египет',
'SV': 'Сальвадор',
'GQ': 'Экваториальная Гвинея',
'ER': 'Эритрея',
'EE': 'Эстония',
'ET': 'Эфиопия',
'FK': 'Фолклендские острова',
'FO': 'Фарерские острова',
'FJ': 'Фиджи',
'FI': 'Финляндия',
'FR': 'Франция',
'GF': 'Французская Гвиана',
'PF': 'Французская Полинезия',
'GA': 'Габон',
'GM': 'Гамбия',
'GE': 'Грузия',
'DE': 'Германия',
'GH': 'Гана',
'GI': 'Гибралтар',
'GR': 'Греция',
'GL': 'Гренландия',
'GD': 'Гренада',
'GP': 'Гваделупа',
'GT': 'Гватемала',
'GN': 'Гвинея',
'GW': 'Гвинея-Бисау',
'GY': 'Гайана',
'HT': 'Гаити',
'VA': 'Ватикан',
'HN': 'Гондурас',
'HK': 'Гонконг',
'HU': 'Венгрия',
'IS': 'Исландия',
'IN': 'Индия',
'ID': 'Индонезия',
'IR': 'Иран',
'IQ': 'Ирак',
'IE': 'Ирландия',
'IM': 'Остров Мэн',
'IL': 'Израиль',
'IT': 'Италия',
'JM': 'Ямайка',
'JP': 'Япония',
'JO': 'Иордания',
'KZ': 'Казахстан',
'KE': 'Кения',
'KW': 'Кувейт',
'KG': 'Кыргызстан',
'LA': 'Лаос',
'LV': 'Латвия',
'LB': 'Ливан',
'LS': 'Лесото',
'LR': 'Либерия',
'LY': 'Джамахирия',
'LI': 'Лихтенштейн',
'LT': 'Литва',
'LU': 'Люксембург',
'MO': 'Макао',
'MK': 'Македония',
'MG': 'Мадагаскар',
'MW': 'Малави',
'MY': 'Малайзия',
'MV': 'Мальдивы',
'ML': 'Мали',
'MT': 'Мальта',
'MH': 'Маршалловы острова',
'MQ': 'Мартиника',
'MR': 'Мавритания',
'MU': 'Маврикий',
'YT': 'Майотта',
'MX': 'Мексика',
'FM': 'Микронезия',
'MD': 'Молдова',
'MC': 'Монако',
'MN': 'Монголия',
'ME': 'Монтенегро',
'MS': 'Монтсеррат',
'MA': 'Марокко',
'MZ': 'Мозамбик',
'MM': 'Мьянма',
'NA': 'Намибия',
'NP': 'Непал',
'NL': 'Нидерланды',
'NC': 'Новая Каледония',
'NZ': 'Новая Зеландия',
'NI': 'Никарагуа',
'NE': 'Нигер',
'NG': 'Нигерия',
'NO': 'Норвегия',
'OM': 'Оман',
'PK': 'Пакистан',
'PW': 'Палау',
'PS': 'Палестина',
'PA': 'Панама',
'PG': 'Папуа - Новая Гвинея',
'PY': 'Парагвай',
'PE': 'Перу',
'PH': 'Филиппины',
'PL': 'Польша',
'PT': 'Португалия',
'QA': 'Катар',
'RO': 'Румыния',
'RU': 'Россия',
'RW': 'Руанда',
'RE': 'Реюньон',
'KR': 'Южная Корея',
'SH': 'Остров Св. Елены',
'KN': 'Сент-Китс и Невис',
'LC': 'Санкт-Люсия',
'MF': 'Сен-Мартен',
'PM': 'Сен-Пьер Микелон',
'VC': 'Святой Винсент и Гренадины',
'WS': 'Самоа',
'SM': 'Сан-Марино',
'ST': 'Сан-Томе и Принсипи',
'SA': 'Саудовская Аравия',
'SN': 'Сенегал',
'RS': 'Сербия',
'SC': 'Сейшельские острова',
'SL': 'Сьерра-Леоне',
'SG': 'Сингапур',
'SX': 'Синт-Мартен',
'SK': 'Словакия',
'SI': 'Словения',
'SB': 'Соломоновы острова',
'SO': 'Сомали',
'ZA': 'Южная Африка',
'SS': 'Южный Судан',
'ES': 'Испания',
'LK': 'Шри-Ланка',
'BL': 'Сен-Барт',
'SD': 'Судан',
'SR': 'Суринам',
'SZ': 'Свазиленд',
'SE': 'Швеция',
'CH': 'Швейцария',
'SY': 'Сирия',
'TW': 'Тайвань',
'TJ': 'Таджикистан',
'TZ': 'Танзания',
'TH': 'Таиланд',
'TL': 'Тимор-Лешти',
'TG': 'Того',
'TT': 'Тринидад и Тобаго',
'TN': 'Тунис',
'TR': 'Турция',
'TC': 'Острова Теркс и Кайкос',
'AE': 'ОАЭ',
'GB': 'Великобритания',
'US': 'США',
'UG': 'Уганда',
'UA': 'Украина',
'UY': 'Уругвай',
'UZ': 'Узбекистан',
'VU': 'Вануату',
'VE': 'Венесуэла',
'VN': 'Вьетнам',
'WF': 'Уоллис и Футуна',
'EH': 'Западная Сахара',
'YE': 'Йемен',
'ZM': 'Замбия',
'ZW': 'Зимбабве'}


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def redirect_country(request):
    # print(request.ipinfo.country)
    ip = get_client_ip(request)
    ipindb = ipCountries.objects.filter(ip=ip)
    if not ipindb:
        country = request.ipinfo.country.lower()
        ipCountries.objects.create(ip=ip, country=country)
        return redirect('/' + country)
    else:
        return redirect('/' + ipindb[0].country)
    # return render(request, 'main/index.html')


def index(request, country):
    if country.upper() not in countries.keys():
        return redirect('/')
    countrydata = CountryStatistics.objects.get(country=country.upper())
    lastupdated = countrydata.updated
    datetime = dt.fromtimestamp(int(lastupdated/1000))
    lastupdatedstring = datetime.strftime('%d.%m.%Y %H:%M:%S')
    print(datetime)
    return render(request, 'main/index.html', {'data': countrydata, 'countryName': countries[country.upper()], 'lastUpdated': lastupdatedstring, 'countryList': countries})


def development(request):
    j = 0
    for i in countries.keys():
        print(j)
        r = requests.get(f'https://disease.sh/v3/covid-19/historical/{i}?lastdays=all').json()
        HistoricData.objects.create(country=i, data=r)
        j += 1
    # print(r[0])
    # for i in r:
    #     if not i['countryInfo']['iso2']:
    #         continue
    #     print("'" + i['countryInfo']['iso2'] + "': " + "'" + i['country'] + "',")
    # j = 0
    # for i in r:
    #     print(j)
    #     if not i['countryInfo']['iso2']:
    #         continue
    #     CountryStatistics.objects.create(country=i['countryInfo']['iso2'], cases=i['cases'], todayCases=i['todayCases'], deaths=i['deaths'], todayDeaths=i['todayDeaths'], recovered=i['recovered'], todayRecovered=i['todayRecovered'], active=i['active'], updated=i['updated'], json=str(i))
    #     j += 1
    return render(request, 'main/index.html')