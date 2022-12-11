from django.contrib import admin
from .models import User, Contact
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date', )
    list_filter = ('created_date', 'email', )
    search_fields = ('subject', 'content')
    sortable_by = ('created_date', 'email', )
