import pytest
from django.contrib.auth import get_user_model
from accounts import models
from rest_framework.test import APIClient

User = get_user_model()


# Authenticated manager and worker fixtures
@pytest.fixture
def authenticated_manager():
    client = APIClient()
    custom_user = User.objects.create_user(
        username='testmanager',
        password='testpassword',
        first_name='Test',
        last_name='Manager'
    )
    manager = models.BusinessManager.objects.create(user=custom_user)
    client.login(username=custom_user.username, password='testpassword')
    client.user = custom_user
    yield client
    if manager:
        manager.delete()

@pytest.fixture
def authenticated_worker():
    client = APIClient()
    worker_user = User.objects.create_user(
        username='testworker',
        password='testpassword',
        first_name='Test',
        last_name='Worker'
    )
    manager_user = User.objects.create_user(
        username='testmanager4',
        password='testpassword',
        first_name='Test',
        last_name='Manager'
    )
    business_manager = models.BusinessManager.objects.create(user=manager_user)
    worker = models.BusinessWorker.objects.create(
        user=worker_user,
        business_manager=business_manager
    )
    client.login(username=worker_user.username, password='testpassword')
    client.user = worker_user
    try:
        yield client
    finally:
        if worker:
            business_manager.delete()

@pytest.fixture
def custom_user():
    user = User.objects.create_user(
        username='testuser',
        password='testpassword',
        first_name='Test',
        last_name='User'
    )
    try:
        yield user
    finally:
        if user.pk:
            user.delete()

@pytest.fixture
def worker():
    worker_user = User.objects.create_user(
        username='testworker2',
        password='testpassword',
        first_name='Test',
        last_name='Worker'
    )
    manager_user = User.objects.create_user(
        username='testmanager5',
        password='testpassword',
        first_name='Test',
        last_name='Manager'
    )
    worker = models.BusinessWorker.objects.create(
        user=worker_user,
        business_manager=models.BusinessManager.objects.create(user=manager_user)
    )
    try:
        yield worker
    finally:    
        if worker.pk:
            worker.delete()

@pytest.fixture
def manager():
    custom_user = User.objects.create_user(
        username='testmanager2',
        password='testpassword',
        first_name='Test',
        last_name='Worker'
    )
    manager = models.BusinessManager.objects.create(user=custom_user)
    yield manager
    if manager.pk:
        manager.delete()

@pytest.fixture
def working_time():
    worker = models.BusinessWorker.objects.create(
        user=User.objects.create_user(
            username='testworker4',
            password='testpassword',
            first_name='Test',
            last_name='Worker'
        ),
        business_manager=models.BusinessManager.objects.create(
            user=User.objects.create_user(
                username='testmanager3',
                password='testpassword',
                first_name='Test',
                last_name='Manager'
            )
        )
    )
    working_time = models.WorkingTime.objects.create(
        start_time='09:00',
        end_time='17:00',
        business_worker=worker
    )
    try:
        yield working_time
    finally:
        if working_time.pk:
            working_time.delete()