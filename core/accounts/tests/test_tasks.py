import pytest
from accounts.tasks.delete_expired_token_task import delete_expired_token

@pytest.mark.django_db
class TestTasks:
    def test_delete_expired_token_task(self):
        """
        Test the delete_expired_token task to ensure it can be called without errors.
        """
        result = delete_expired_token()
        assert result == "Expired tokens deleted successfully"