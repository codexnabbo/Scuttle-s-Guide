from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.
def lol_home_view(request, *args, **kwargs):
    return render(request, "lol_home.html",{'name' : "utente"})