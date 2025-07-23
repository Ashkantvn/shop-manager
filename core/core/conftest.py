import pytest 
from django.conf import settings


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": settings.CELERY_BROKER_URL,
        "result_backend": settings.CELERY_RESULT_BACKEND,
    }

@pytest.fixture(scope="session")
def celery_worker_parameters():
    return {
        "queues": ("default",),     
        "concurrency": 1            
    }