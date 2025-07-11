import pytest
from accounts import models
from accounts.tests.fixtures import (
    custom_user, 
    worker, 
    manager, 
    working_time,
    blacklist_access_token,
    )

@pytest.mark.django_db
class TestAccountsModels:

    # test user model 
    def test_custom_user_model_is_created(self):
        user = models.CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        assert isinstance(user, models.CustomUser)
        assert user.pk is not None
        assert user.first_name == 'Test'
        assert user.last_name == 'User'
        assert user.username == 'testuser'
        assert user.check_password('testpassword')
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False
    
    def test_custom_user_str_method(self, custom_user):
        assert str(custom_user) == f"{custom_user.first_name} {custom_user.last_name}"
    
    # test business worker model
    def test_business_worker_model_is_created(self, worker):
        assert worker.pk is not None
        assert isinstance(worker.business_manager, models.BusinessManager)
        assert isinstance(worker.user, models.CustomUser)

    def test_business_worker_str_method(self, worker):
        assert str(worker) == f"{worker.user.first_name} {worker.user.last_name}"
    
    # test working time model
    def test_working_time_model_is_created(self, working_time):
        assert isinstance(working_time, models.WorkingTime)
        assert working_time.pk is not None
        assert working_time.start_time == '09:00'
        assert working_time.end_time == '17:00'

    def test_working_time_str_method(self, working_time):
        assert str(working_time) == f"{working_time.start_time} - {working_time.end_time} for {working_time.business_worker.user.first_name} {working_time.business_worker.user.last_name}"

    # test business manager model
    def test_business_manager_model_is_created(self,manager):
        assert manager.pk is not None
        assert isinstance(manager, models.BusinessManager)
        assert isinstance(manager.user, models.CustomUser)
        assert manager.user.username == 'testmanager2'
        assert manager.user.check_password('testpassword')

    def test_business_manager_str_method(self, manager):
        assert str(manager) == f"{manager.user.first_name} {manager.user.last_name}"

    # Test blacklist access token model
    def test_blacklist_access_token_model_is_created(self, blacklist_access_token):
        assert blacklist_access_token.pk is not None
        assert isinstance(blacklist_access_token, models.AccessTokenBlackList)
        assert isinstance(blacklist_access_token.token, str)
        assert blacklist_access_token.expire_date is not None

    def test_blacklist_access_token_str_method(self, blacklist_access_token):
        assert str(blacklist_access_token) == f"Token: {blacklist_access_token.token}, Expire Date: {blacklist_access_token.expire_date}"