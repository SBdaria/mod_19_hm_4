from django.contrib import admin
from .models import Buyer, Game

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    search_fields = ('title',)
    list_filter = ('age_limited',)
