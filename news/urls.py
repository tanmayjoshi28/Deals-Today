from django.conf.urls import url
from .views import scrapef, view_home, scrapeA

urlpatterns = [

    url(r'^scrapef/', scrapef, name="scrapef"),
    url(r'^home/', view_home, name='home'),
    url(r'^scrapeA/', scrapeA, name="scrapeA")

]