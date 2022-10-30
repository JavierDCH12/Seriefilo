from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'updated_at', 'created_at')
    ordering = ('created_at',)



admin.site.register(Page, PageAdmin)
