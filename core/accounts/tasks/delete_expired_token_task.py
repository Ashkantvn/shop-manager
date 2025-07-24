import celery

@celery.shared_task
def delete_expired_token():
    pass