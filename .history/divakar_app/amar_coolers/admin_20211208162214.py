from django.contrib import admin
from . models import Inquiry
# Register your models here.

class BookInquiry(admin.ModelAdmin):
    list_display=('date','name','inquiry','modile')

class BookUser(admin.ModelAdmin):
    list_display=('user','date')
admin.site.register(Inquiry,BookInquiry)
