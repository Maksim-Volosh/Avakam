from celery import shared_task
from .models import Advertisement

@shared_task
def delete_expired_advertisements():
    expired_ads = Advertisement.objects.all()
    count = 0
    for ad in expired_ads:
        if ad.is_expired():
            count += 1
            ad.delete()
    return count
