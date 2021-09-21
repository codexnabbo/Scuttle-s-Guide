from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
import json
import requests
# Create your views here.

CHAMP_COUNT = 0

# cambio i nomi strani in nomi accettati dal server di lol
def Check(i):
    i = i.replace(" ", "")
    i = i.replace("\'", "")
    i = i.replace(".", "")
    if i == "ChoGath" or i == "KaiSa" or i == "KhaZix" or i == "LeBlanc" or i == "VelKoz":
        i = i.capitalize()
    elif i == "Wukong":
        i = "MonkeyKing"
    elif i == "Nunu&Willump":
        i = "Nunu"

    return i


def lol_home_view(request, *args, **kwargs):
    # uso il file json con le patch per prendere l'ultima patch
    url_patch = "https://ddragon.leagueoflegends.com/api/versions.json"
    patch = requests.get(url_patch)
    text = patch.text
    data = json.loads(text)
    # imposto l'ultima patch come patch per i dati e li prendo
    url = "https://ddragon.leagueoflegends.com/cdn/" +data[0]+"/data/en_US/champion.json"
    patch = data[0]
    all_champ_json = requests.get(url)
    text = all_champ_json.text
    data = json.loads(text)
    champions = []
    CHAMP_COUNT = len(data["data"])
    #creo un array con tutti i nomi dei campioni
    for i in data["data"]:
        champions.append(data["data"][i]["name"])
    # creo un array con i nomi per le immagini(servono i nomi senza caratteri strani)
    all_image = []
    for i in champions:
        i = Check(i)
        all_image.append(i)
    # ritorno la pagina home di lol con alcune variabili che mi serviranno
    return render(request, "lol_home.html", {'img' : all_image, "patch": patch})
