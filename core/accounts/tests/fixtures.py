import pytest
from django.contrib.auth import get_user_model
from accounts import models

User = get_user_model()


@pytest.fixture
def custom_user():
    user = User.objects.create_user(
        username='testuser',
        password='testpassword',
        first_name='Test',
        last_name='User'
    )
    yield user
    if user.pk:
        user.delete()

@pytest.fixture
def worker(custom_user):
    worker = models.BusinessWorker.objects.create(
        user=custom_user,
        manager=models.BusinessManager.objects.create(user=custom_user)
    )
    yield worker
    if worker.pk:
        worker.delete()

@pytest.fixture
def manager(custom_user):
    manager = models.BusinessManager.objects.create(user=custom_user)
    yield manager
    if manager.pk:
        manager.delete()

@pytest.fixture
def working_time(worker):
    working_time = models.WorkingTime.objects.create(
        start_time='09:00',
        end_time='17:00',
        business_worker=worker
    )
    yield working_time
    if working_time.pk:
        working_time.delete()