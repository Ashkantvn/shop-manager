from django.db import models



class AccessTokenBlackList(models.Model):
    token = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return f"Token: {self.token}"