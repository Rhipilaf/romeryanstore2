from django.contrib import admin

from shop.models import Purchases, Account

@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'account',
        'number_purchase',
        'platform',
        'login',
        'password',
        'time'
    ]

    search_fields = [
        'id',
        'account',
        'number_purchase'
    ]

    list_filter = [
        'platform'
    ]

    ordering = [
        'platform'
    ]

    save_as = True
    save_on_top = True

@admin.register(Account)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'full_description',
        'price',
        'availability',
        'sales',
        'platform',
        'type',
        'get_img_admin'
    ]

    search_fields = [
        'id',
        'title'
    ]

    list_filter = [
        'platform'
    ]

    ordering = [
        'platform'
    ]

    save_as = True
    save_on_top = True

