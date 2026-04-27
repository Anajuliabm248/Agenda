from django.contrib import admin
from contact import models

# configuração do model no admin
#vizualização da tabela contact no painel admin

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'created_date', 'category', 'show',
    ordering = 'id',
    search_fields = 'first_name', 'id',
    list_editable = 'first_name', 'last_name', 'email', 'category', 'show',
    list_per_page = 5
    list_max_show_all = 100

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    ordering = 'id',
    search_fields = 'name',
    list_per_page = 5
    list_max_show_all = 100
    list_editable = 'name',
