from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Comment)
class hotel(admin.ModelAdmin):
    list_display = ('name','email')
