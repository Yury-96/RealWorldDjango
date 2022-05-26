from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventdAdmin(admin.ModelAdmin):
  pass


@admin.register(models.Category)
class CategorydAdmin(admin.ModelAdmin):
  pass
# Register your models here.
