from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html",{'name' : "utente"})