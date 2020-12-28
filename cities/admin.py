from django.contrib import admin
from .models import Country, City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'population')
    list_filter = ('country',)

admin.site.register(Country)
admin.site.register(City, CityAdmin)
