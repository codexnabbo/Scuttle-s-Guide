from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.
def valorant_home_view(request, *args, **kwargs):
    return render(request, "valorant_home.html",{'name' : "utente"})