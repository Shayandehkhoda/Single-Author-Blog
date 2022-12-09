from django.contrib import admin
from .models import User, Contact
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass