from datetime import timedelta

from django.db import models
from django.utils import timezone


class Advertisement(models.Model):
    title = models.CharField('title', max_length=120)
    banner = models.ImageField('Banner photo',upload_to='advertisement_banners')
    url = models.URLField('url of site or other link')
    created_at = models.DateTimeField('Date of creation', auto_now_add=True)
    duration = models.IntegerField('duration in days', choices=[(1, '1 days'), (2, '2 days'), (3, '3 days'), (7, '7 days'), (14, '14 days'), (30, '30 days')])
    
    def expiration_date(self):
        """ Calculate the expiration date based on the duration. """
        return self.created_at + timedelta(days=self.duration)
    
    def is_expired(self):
        """ Check if the advertisement is expired. """
        return timezone.now() > self.expiration_date()
    
    def __str__(self):
        return self.title
