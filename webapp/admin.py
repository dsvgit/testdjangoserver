from django.contrib import admin
from webapp import models

admin.site.register(models.Organization)
admin.site.register(models.User)
admin.site.register(models.Purchase)