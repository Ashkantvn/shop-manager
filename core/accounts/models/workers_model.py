from django.db import models


class BusinessWorker(models.Model):
    user = models.OneToOneField(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="business_workers"
    )
    business_manager = models.ForeignKey(
        "accounts.BusinessManager",
        on_delete=models.CASCADE,
        related_name="workers"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Business Worker"
        verbose_name_plural = "Business Workers"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
