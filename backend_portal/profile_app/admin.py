from django.contrib import admin
from .models import Contact, Profile, Task

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')  
    search_fields = ('name', 'email')          
    list_filter = ('email',)                  



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields] 
    search_fields = ('title', 'description') 
