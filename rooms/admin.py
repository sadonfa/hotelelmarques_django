from django.contrib import admin
from rooms.models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_filter = ('id',)
    list_display = ('title', 'image', 'create_ad', 'update_ad')

admin.site.register(Room, RoomAdmin)

admin.site.site_header = "Hotel El Marques de Manga"
admin.site.site_title = "Hotel El Marques de Manga"
admin.site.index_title = "Panel De Hotel El Marques de Manga"