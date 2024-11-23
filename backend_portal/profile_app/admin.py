# profile_app/admin.py
from django.contrib import admin
from .models import Contact, Profile, Task

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')  # Spalten in der Liste
    search_fields = ('name', 'email')          # Suchfelder
    list_filter = ('email',)                   # Filteroptionen



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Nur den User anzeigen


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]  # Alle Felder dynamisch einfügen
    search_fields = ('title', 'description')  # Suchfelder
