from django.contrib import admin

from ..models import Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    ...
