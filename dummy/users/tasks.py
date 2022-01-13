from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

@celery_app.task()
def get_users_list():
    """A pointless Celery task to demonstrate usage."""
    return [user.username for user in User.objects.all()]

@celery_app.task()
def get_users_list_with_id():
    """A pointless Celery task to demonstrate usage."""
    return [(user.username, user.id) for user in User.objects.all()]