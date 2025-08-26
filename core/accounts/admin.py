from django.contrib import admin
from accounts import models
# Register your models here.
admin.site.register([models.AccessTokenBlackList,models.CustomUser, models.BusinessManager, models.BusinessWorker, models.WorkingTime])



