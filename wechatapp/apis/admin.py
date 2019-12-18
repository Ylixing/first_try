#!/usr/bin/python
# -*- encoding=utf-8 -*-


import hashlib

from django.contrib import admin
from .models import App

# Register your models here.

# admin.site.register(App)

@admin.register(App)
class APisAppAdmin(admin.ModelAdmin):

    # 指定显示信息
    fields = ['name', 'application', 'category', 'url', 'publish_date',
              'desc']
    pass

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        appid = hashlib.md5(src.encode('utf8')).hexdigest()
        obj.appid = appid
        super().save_model(request, obj, form, change)
