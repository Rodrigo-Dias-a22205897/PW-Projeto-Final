import requests
from functools import lru_cache
import time
from django.shortcuts import render
from django.http import JsonResponse


url_regions = "https://api.ipma.pt/open-data/distrits-islands.json"
url_descricaoTempo = "https://api.ipma.pt/open-data/weather-type-classe.json"
url_warnings = "https://api.ipma.pt/open-data/forecast/warnings/warnings_www.json"

@lru_cache(maxsize=None)
def get_json(url):
    headers = {
      'User-Agent': 'Radar do Tempo (https://a22205897.pythonanywhere.com/meteo/)',
      'From': 'a22205897@alunos.ulht.pt'
    }
    t = 1

    response = requests.get(url,headers,verify = False)

    while response.status_code == 429:
      t **= 2
      time.sleep(t)
      response = requests.get(url,headers,verify = False)

    if response.status_code == 200:
        return response.json()

def get_descricao(id):
    tipos = get_json(url_descricaoTempo)
    for info in tipos['data']:
        if info['idWeatherType'] == id:
            return info["descWeatherTypePT"]

def get_warning_region(idAreaAviso):
    data = get_json(url_warnings)
    avisos = []
    for info in data:
        if info['idAreaAviso'] == idAreaAviso:
            aviso = {
                "awarenessLevelID": info['awarenessLevelID'],
                "awarenessTypeName": info['awarenessTypeName'],
            }
            avisos.append(aviso)
    return avisos

def get_color(avisos):
    for aviso in avisos:
        if aviso["awarenessLevelID"] in ("red", "yellow", "orange"):
            return aviso["awarenessLevelID"]
    return "green"

def get_region_name(globalIdLocal):
    lista = get_regions()
    for info in lista['regioes']:
        if info['globalIdLocal'] == globalIdLocal:
            return info["local"]

def get_regions():
    data = get_json(url_regions)
    lista = {"pais": "Portugal", "regioes": []}
    for info in data['data']:
        regiao = {
            "local": info['local'],
            "globalIdLocal": info['globalIdLocal'],
            "color": get_color(get_warning_region(info['idAreaAviso'])),
        }
        lista["regioes"].append(regiao)
    return lista

def get_weather_data(globalIdLocal):
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json"
    data = get_json(url)
    previsao_lisboa = {"cidade": get_region_name(globalIdLocal), "previsoes": []}
    for forecast in data['data']:
        previsao = {
            "data": forecast['forecastDate'],
            "temperatura_maxima": forecast['tMax'],
            "temperatura_minima": forecast['tMin'],
            "precipitacao": forecast['precipitaProb'],
            "id": forecast['idWeatherType'],
            "descricao": get_descricao(forecast['idWeatherType']),
        }
        previsao_lisboa["previsoes"].append(previsao)
    return previsao_lisboa

def get_diaHoje_previsao(previsoes):
    if previsoes:
        return previsoes[0]
    else:
        return None

def index_view(request):
    lista = get_regions()
    return render(request, "meteo/index.html", lista)

def api_view(request):
    return render(request, "meteo/API.html")

def previsao_view(request, globalIdLocal):
    previsao_lisboa = get_weather_data(globalIdLocal)
    return render(request, "meteo/previsao.html", previsao_lisboa)

def cidades_view(request):
    lista = get_regions()
    return JsonResponse(lista)

def api_previsao_hoje_view(request, globalIdLocal):
    previsao_lisboa = get_weather_data(globalIdLocal)
    primeira_previsao = get_diaHoje_previsao(previsao_lisboa["previsoes"])
    return JsonResponse(primeira_previsao)

def api_previsao_semana_view(request, globalIdLocal):
    previsao_lisboa = get_weather_data(globalIdLocal)
    return JsonResponse(previsao_lisboa)

def api_img_view(request):
    previsao_lisboa = get_weather_data(1110600)
    primeira_previsao = get_diaHoje_previsao(previsao_lisboa["previsoes"])
    if primeira_previsao['id'] < 10:
        scr = f"https://a22205897.pythonanywhere.com/static/meteo/w_ic_d_0{primeira_previsao['id']}anim.svg"
        response = { 'src' : scr }
    else:
        scr = f"https://a22205897.pythonanywhere.com/static/meteo/w_ic_d_{primeira_previsao['id']}anim.svg"
        response = { 'src' : scr }
    return JsonResponse(response)