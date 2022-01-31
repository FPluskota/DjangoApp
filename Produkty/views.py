from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria


# Create your views here.


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)

def produkt (request, id):
    produkt_user = Produkty.objects.get(pk=id)
    napis= "<h1>"+ str(produkt_user) +"</h1>" \
           "<p>"+ str(produkt_user.opis) +"</p>" \
           "<p>" + str(produkt_user.cena)+ "</p>"
