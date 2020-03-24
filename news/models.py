from django.db import models
from django.conf import settings


class TopDealFlipkart(models.Model):
    title = models.CharField(max_length= 100)
    price = models.CharField(max_length= 100)
    url = models.TextField()

    def __str__(self):
        return self.title


class TopDealAmazon(models.Model):
    title = models.CharField(max_length= 100)
    price = models.CharField(max_length= 100)
    url = models.TextField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_scrape = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return "{}-{}".format(self.user, self.last_scrape)

