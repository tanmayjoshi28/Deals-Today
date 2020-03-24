from django.contrib import admin
from .models import TopDealAmazon, TopDealFlipkart, UserProfile
admin.site.register(UserProfile)
admin.site.register(TopDealFlipkart)
admin.site.register(TopDealAmazon)
# Register your models here.
