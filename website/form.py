from django.contrib import admin
from .models import HeaderObject
from .admin import HeaderObjectForm


@admin.register(HeaderObject)
class HeaderObjectAdmin(admin.ModelAdmin):
    form = HeaderObjectForm
