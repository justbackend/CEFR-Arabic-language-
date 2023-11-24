from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Time_Settings)


# admin.site.register(Subscription)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'date_joined')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'end_date', 'start_date']
    search_fields = ['user__username']
    list_filter = ['end_date']
    ordering = ['end_date']
    search_help_text = "Foydalanuvchi ismi bo'yicha qidiring"
    autocomplete_fields = ['user']


@admin.register(Part1)
class Part1Admin(admin.ModelAdmin):
    list_display = ['question', 'id']
    list_display_links = ['question']
    search_fields = ['id', 'question']


@admin.register(Part2)
class Part2Admin(admin.ModelAdmin):
    list_display = ['topic', 'id']
    list_display_links = ['topic']
    search_fields = ['id', 'topic']


@admin.register(Part3)
class Part3Admin(admin.ModelAdmin):
    list_display = ['topic', 'id']
    list_display_links = ['topic']
    search_fields = ['id', 'topic']


admin.site.register(JuzAudio)
admin.site.register(TestTaker)
admin.site.register(DoNotEnter)
