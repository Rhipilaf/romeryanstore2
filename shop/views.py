
from django.shortcuts import render

from shop.models import Purchases, Account, Info, Case, PlatformAccount, TypeAccount


def render_home(request):
    title = request.GET.get('title', )
    type = request.GET.get('type', )

    accounts = Account.objects.all()
    type = Account.objects.all()

    # accounts_list = Account.object.all()
    if title:
       accounts = accounts.filter(title__icontains=title)
    # if type:
    #    accounts = accounts.filter(type__id=type)
    return render(request, "home.html", {'accounts': accounts, 'title': title,
                                         'tipi_acccount': TypeAccount.objects.all(),
                                         'platformi':PlatformAccount.objects.all()  })

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
    cases = Case.objects.all()
    return render(request, "cases.html", {'cases': cases})

def render_info(request):
    infos = Info.objects.all()
    return render(request, "home.html", {'info': infos})

def render_case(request, id_case):
    case = Case.objects.get(id=id_case)
    return render(request, "case.html", {'case': case})

