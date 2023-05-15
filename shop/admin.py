from django.contrib import admin

from shop.models import Purchases, Account, Info, Polzovatel, Case, GameInCase, TypeAccount, PlatformAccount


class PurchasesInline(admin.TabularInline):
    model = Purchases
    extra = 0

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
        'platform_fk',
        'type_fk',
        'get_img_admin'
    ]

    search_fields = [
        'id',
        'title'
    ]

    list_filter = [
        'platform_fk'
    ]

    ordering = [
        'platform_fk'
    ]

    save_as = True
    save_on_top = True

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
    ]

@admin.register(Polzovatel)
class PolzovatelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nickname',
        'image',
        'mail'
    ]
    inlines = [PurchasesInline]


class GameInCaseInline(admin.TabularInline):
    model = GameInCase
    extra = 0
    autocomplete_fields = [
        'account'
    ]

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
    ]
    inlines = [GameInCaseInline]

@admin.register(TypeAccount)
class TypeAccountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]

@admin.register(PlatformAccount)
class TypeAccountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
