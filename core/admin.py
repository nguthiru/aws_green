from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.gis import admin as geo_admin


class LocationModelAdmin(geo_admin.OSMGeoAdmin):
    list_display = ("id", "name","location")
    list_display_links = ("id", "name","location")


admin.site.register([TreeShop, RecycleArea,
                    Campaign, ], LocationModelAdmin)
admin.site.register([CampaignInvolvement,Tree,TreeOrder])