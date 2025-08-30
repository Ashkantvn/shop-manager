from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_slug',)}),
    )
    readonly_fields = ('user_slug','created_date','updated_date')
    list_display = ('username', 'first_name', 'last_name', 'user_slug', 'created_date','updated_date')


admin.site.register(models.CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register([models.AccessTokenBlackList, models.BusinessManager, models.BusinessWorker, models.WorkingTime])



