from django.contrib import admin
from .models import TBCars

class TBCarsAdmin(admin.ModelAdmin):
    list_display = ('carname', 'carbrand', 'carmodel', 'carprice')
    search_fields = ('carname', 'carbrand')

admin.site.register(TBCars, TBCarsAdmin)