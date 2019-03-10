from django.contrib import admin

# Register your models here.
from .forms import StatusForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = StatusForm


admin.site.register(Status, StatusAdmin)
