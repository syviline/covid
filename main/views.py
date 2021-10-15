from django.shortcuts import render, redirect, HttpResponse
from .models import CountryStatistics, ipCountries, HistoricData, Regions
import requests
from datetime import datetime as dt
import json
import time


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
    historicdata = HistoricData.objects.filter(country=country.upper())
    history = ''
    if not historicdata:
        history = 'no_data'
    historicdata = historicdata[0]
    if time.time() - historicdata.updatedClient > 3600:
        if country.lower() != 'world':
            r = requests.get(f'https://disease.sh/v3/covid-19/historical/{country}?lastdays=all').json()
        else:
            newr = requests.get('https://disease.sh/v3/covid-19/historical/all?lastdays=all').json()
            r = {"timeline": newr}
        historicdata.data = json.dumps(r)
        historicdata.updatedClient = time.time()
        historicdata.save()
    history = json.loads(historicdata.data)
    if 'message' in history:
        history = 'no_data'
    countrydata = CountryStatistics.objects.get(country=country.upper())
    if time.time() - countrydata.updatedClient > 3600:
        if country.lower() != 'world':
            r = requests.get(f'https://disease.sh/v3/covid-19/countries/{country}?strict=true').json()
        else:
            r = requests.get('https://disease.sh/v3/covid-19/all').json()
        countrydata.cases = r['cases']
        countrydata.todayCases = r['todayCases']
        countrydata.deaths = r['deaths']
        countrydata.todayDeaths = r['todayDeaths']
        countrydata.recovered = r['recovered']
        countrydata.todayRecovered = r['todayRecovered']
        countrydata.active = r['active']
        countrydata.updated = r['updated']
        countrydata.updatedClient = time.time()
        countrydata.json = str(r)
        countrydata.save()
    lastupdated = countrydata.updated
    topCases = '{}'
    topDeaths = '{}'
    if country == 'world':
        topCasesDB = CountryStatistics.objects.all().order_by('-cases').exclude(country='WORLD')[:10]
        topDeathsDB = CountryStatistics.objects.all().order_by('-deaths').exclude(country='WORLD')[:10]
        topCases = {}
        topDeaths = {}
        for i in topCasesDB:
            topCases[countries[i.country]] = i.cases
        for i in topDeathsDB:
            topDeaths[countries[i.country]] = i.deaths
    datetime = dt.fromtimestamp(int(lastupdated/1000))
    lastupdatedstring = datetime.strftime('%d.%m.%Y %H:%M:%S')
    return render(request, 'main/index.html', {'data': countrydata, 'countryName': countries[country.upper()], 'lastUpdated': lastupdatedstring, 'countryList': countries, 'history': history, 'topCases': str(topCases), 'topDeaths': str(topDeaths)})


def getHistoricalStatistics(request, country, timespan):
    data = HistoricData.objects.filter(country=country.upper())
    if not data:
        return HttpResponse(json.dumps({'error': 'country not found'}))
    data = json.loads(data)
    if 'message' in data:
        return HttpResponse('no_data')
    return HttpResponse(1)


def development(request):
    # j = 0
    # for i in countries.keys():
    #     print(j)
    #     r = requests.get(f'https://disease.sh/v3/covid-19/historical/{i}?lastdays=all').json()
    #     HistoricData.objects.create(country=i, data=r)
    #     j += 1
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
    # for i in HistoricData.objects.all():
    #     i.data = i.data.replace("'", '"')
    #     i.save()
    a = CountryStatistics.objects.all().order_by('-cases').exclude(country='WORLD')[:10]
    for i in a:
        print(i.country)
    return render(request, 'main/index.html')


def region(request):
    # r = requests.get('https://milab.s3.yandex.net/2020/covid19-stat/data/v10/default_data.json').json()
    # print(json.dumps(r['russia_stat_struct']['data']))
    # Regions.objects.create(data=json.dumps(r['russia_stat_struct']['data']), lastUpdated=time.time())
    data = Regions.objects.get(id=1)
    if time.time() - data.lastUpdated > 3600:
        r = requests.get('https://milab.s3.yandex.net/2020/covid19-stat/data/v10/default_data.json').json()
        newr = {}
        for i in r['russia_stat_struct']['data'].keys():
            if i == '225':
                continue
            d = r['russia_stat_struct']['data'][i]['info']
            newr[d['name']] = {'population': d['population'], 'cases': d['cases'], 'cases_delta': d['cases_delta'], 'deaths': d['deaths'], 'deaths_delta': d['deaths_delta'], 'date': d['date']}
        print(newr)
        data.data = json.dumps(newr)
        data.lastUpdated = time.time()
        data.save()
    a = json.loads(data.data)
    return render(request, 'main/region.html', {'data': a})