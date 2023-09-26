from django.contrib import admin
from .models import DataTest

# admin.site.register(DataTest)

@admin.register(DataTest)
class DataSetAdimin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at',]


