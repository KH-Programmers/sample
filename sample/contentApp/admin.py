from django.contrib import admin
from .models import contentModel

class contentModelAdmin(admin.ModelAdmin):
    list_display = ("id","Title","date")
admin.site.register(contentModel,contentModelAdmin)
# Register your models here.
