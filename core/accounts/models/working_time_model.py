from django.db import models

class WorkingTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    business_worker = models.ForeignKey(
        'accounts.BusinessWorker',
        on_delete=models.CASCADE,
        related_name='working_times'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Working Time'
        verbose_name_plural = 'Working Times'

    def __str__(self):
        return f"{self.start_time} - {self.end_time} for {self.business_worker.user.first_name} {self.business_worker.user.last_name}"