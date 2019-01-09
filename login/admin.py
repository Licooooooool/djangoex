from django.contrib import admin
from . import models

admin.site.register(models.User)


admin.site.site_header = '餐饮管理系统'
admin.site.site_title = '餐饮管理系统'