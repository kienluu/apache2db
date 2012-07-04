from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apachelog.models import Log

class LogAdmin(ModelAdmin):
	pass

admin.site.register(Log, LogAdmin)