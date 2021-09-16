from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request

# Create your views here.
def r6_home_view(request, *args, **kwargs):
    return render(request, "r6_home.html",{'name' : "utente"})