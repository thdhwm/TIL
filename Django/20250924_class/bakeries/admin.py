from django.contrib import admin
from .models import Bakery
# from bakeries.models import Bakery

# admin.site.register(Bakery)

@admin.register(Bakery)
class BakeryAdmin(admin.ModelAdmin):
    list_display = ("name", "rating")
