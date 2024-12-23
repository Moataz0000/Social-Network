from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'created', 'modifiyed', 'available']
    list_filter = ['available']
    search_fields = ['user', 'bio']