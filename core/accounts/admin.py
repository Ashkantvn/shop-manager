from django.contrib import admin
from accounts import models
# Register your models here.
admin.site.register([models.CustomUser, models.BusinessManager, models.BusinessWorker, models.WorkingTime])