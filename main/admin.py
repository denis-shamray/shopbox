from django.contrib import admin
from main.models import Good
from main.models import Picture

class GoodAdmin(admin.ModelAdmin):
   fieldsets = (
      (None, {
         'fields': ('title', 'short', 'price', 'options_text', 'details')
      }),
   )
admin.site.register(Good, GoodAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'preview', 'created_at', 'updated_at')


admin.site.register(Picture, PictureAdmin)
# Register your models here.
