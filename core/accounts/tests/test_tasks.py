import pytest
from accounts.models import AccessTokenBlackList
from accounts.tasks.delete_expired_token_task import delete_expired_token


@pytest.mark.celery
def test_delete_expired_token_task(celery_app, celery_worker):
    """
    Test the delete_expired_token task to ensure it can be called without errors.
    """
    result = delete_expired_token.delay().get(timeout=10)
    assert result.successful()  # Ensure the task was executed successfully