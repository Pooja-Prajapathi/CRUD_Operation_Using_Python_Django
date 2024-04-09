from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = ("userid","username","email","password")

