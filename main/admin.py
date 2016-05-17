from django.contrib import admin
from main.models import Good
from main.models import Picture
from main.models import Category
from main.models import Zakaz
from main.models import Msg
from main.models import Ico
from main.models import Sms
from main.models import Variable

class GoodAdmin(admin.ModelAdmin):
   fieldsets = (
      (None, {
         'fields': ('title', 'short', 'price', 'details', 'category')
      }),
   )
admin.site.register(Good, GoodAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'good_title', 'preview', 'created_at', 'updated_at')


admin.site.register(Picture, PictureAdmin)


class IcoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'preview', 'created_at', 'updated_at')


admin.site.register(Ico, IcoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(Category, CategoryAdmin)


class ZakazAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'tel', 'place', 'cart', 'state', 'created_at', 'updated_at')


admin.site.register(Zakaz, ZakazAdmin)

                                                                       
class MsgAdmin(admin.ModelAdmin):
    list_display = ('username', 'useremail', 'userphone', 'usermsg', 'state', 'created_at', 'updated_at')


admin.site.register(Msg, MsgAdmin)


class SmsAdmin(admin.ModelAdmin):
    list_display = ('username', 'useremail', 'userphone', 'userplace', 'state', 'userfile', 'created_at', 'updated_at')


admin.site.register(Sms, SmsAdmin)


class VariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'value')


admin.site.register(Variable, VariableAdmin)
# Register your models here.