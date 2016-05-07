from django.contrib import admin
from main.models import Good
from main.models import Picture
from main.models import Category
from main.models import Zakaz
from main.models import Msg

class GoodAdmin(admin.ModelAdmin):
   fieldsets = (
      (None, {
         'fields': ('title', 'short', 'price', 'options_text', 'details', 'category')
      }),
   )
admin.site.register(Good, GoodAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'good_title', 'preview', 'created_at', 'updated_at')


admin.site.register(Picture, PictureAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(Category, CategoryAdmin)


class ZakazAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'tel', 'place', 'cart', 'state', 'created_at', 'updated_at')


admin.site.register(Zakaz, ZakazAdmin)


class MsgAdmin(admin.ModelAdmin):
    list_display = ('username', 'useremail', 'userphone', 'usermsg', 'state', 'created_at', 'updated_at')


admin.site.register(Msg, MsgAdmin)
# Register your models here.