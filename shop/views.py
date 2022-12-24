
from django.shortcuts import render

from shop.models import Purchases, Account, Info


def render_home(request):
    accounts = Account.objects.all()
    return render(request, "home.html", {'accounts': accounts})

def render_user(request):
    purchases = Purchases.objects.all()
    return render(request, "user.html", {'purchases': purchases})

def render_game(request):
    accounts = Account.objects.all()
    return render(request, "game.html", {'accounts': accounts})

def render_agreement(request):
    return render(request, "agreement.html", {})

def render_detail_game(request, id_game):
    account = Account.objects.get(id=id_game)
    return render(request, "game.html", {'account': account})

def render_cases(request):
    return render(request, "cases.html", {})

def render_info(request):
    infos = Info.objects.all()
    return render(request, "home.html", {'info': infos})
