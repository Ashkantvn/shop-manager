from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Other information", {'fields': ('user_slug','created_date','updated_date')}),
    )
    readonly_fields = ('user_slug','created_date','updated_date','date_joined','last_login')


admin.site.register(models.CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register([models.AccessTokenBlackList, models.BusinessManager, models.BusinessWorker, models.WorkingTime])



