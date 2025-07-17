from django.db import models



class AccessTokenBlackList(models.Model):
    token = models.CharField(max_length=255)

    def __str__(self):
        return f"Token: {self.token}"