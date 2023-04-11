"""romeryanstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.api import Login, Logout, Registration, PolzovatelChangePhoto
from shop.views import render_home, render_user, render_game, render_agreement, render_detail_game, render_cases, \
    render_case

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cases', render_cases),
    path('case/<id_case>', render_case, name="render_detail_case"),
    path('game/<id_game>', render_detail_game, name="render_detail_game"),
    path('agreement', render_agreement),
    path('game', render_game),
    path('purchases', render_user),
    path('login', Login.as_view(), name='kabinet_login'),
    path('logout', Logout.as_view(), name='kabinet_logout'),
    path('registration', Registration.as_view(), name='kabinet_registration'),
    path('change_photo', PolzovatelChangePhoto.as_view(), name='change_photo'),
    path('', render_home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)