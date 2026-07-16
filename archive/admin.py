from django.contrib import admin
from .models import Level,Myth

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'depth_score')

@admin.register(Myth)
class MythAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
