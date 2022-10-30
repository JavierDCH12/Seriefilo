from django.contrib import admin
from .models import Serie, Category, Platform

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('genre', 'description')
    list_display = ('genre', )
    ordering = ('genre',)




class PlatformAdmin(admin.ModelAdmin):
    search_fields = ('wheretosee',)
    list_display = ('wheretosee', )
    ordering = ('wheretosee',)


class SerieAdmin(admin.ModelAdmin):

    readonly_fields = ('user',)
    search_fields = ('title', 'description', 'user')
    list_display = ('title', 'user', 'visible') 
    list_filter = ('user', 'visible', 'categories', 'platform')
    



    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()





admin.site.register(Serie, SerieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)



# Register your models here.
