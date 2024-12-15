from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'model', 'year', 'price', 'brand')
    list_display_links = ('id', 'model')
    list_editable = ('price', 'brand')
    list_filter = ('brand', 'model')
    search_fields = ('model', 'year')


admin.site.register(Brand)
admin.site.register(Cars, CarAdmin)
