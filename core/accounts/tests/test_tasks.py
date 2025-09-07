import pytest
from accounts.tasks import delete_expired_token


@pytest.mark.django_db
class TestTasks:

    # Tests for the delete_expired_token task
    def test_delete_expired_token_task(self):
        """
        Test the delete_expired_token task
        to ensure it can be called without errors.
        """
        result = delete_expired_token()
        assert result == "Expired tokens deleted successfully"

    def test_delete_expired_token_task_celery(self):
        """
        Test the delete_expired_token task
        to ensure it can be called without errors.
        """
        async_result = delete_expired_token.apply_async()
        result = async_result.get(timeout=10)
        assert result == "Expired tokens deleted successfully"
