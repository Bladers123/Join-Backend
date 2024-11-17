# profile_app/admin.py
from django.contrib import admin
from .models import Contact, Profile, Ticket

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')  # Spalten in der Liste
    search_fields = ('name', 'email')          # Suchfelder
    list_filter = ('email',)                   # Filteroptionen



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Nur den User anzeigen


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ticket._meta.fields]  # Alle Felder dynamisch einfügen
    search_fields = ('title', 'description')  # Suchfelder
