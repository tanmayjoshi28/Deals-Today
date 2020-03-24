from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import urllib3
from .models import UserProfile, TopDealFlipkart, TopDealAmazon
from datetime import timezone, datetime, timedelta
import math
urllib3.disable_warnings()


def scrapef(request):
    session = requests.Session()
    session.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    user_p = UserProfile.objects.filter(user=request.user).first()
    if user_p is not None:
        user_p.last_scrape = datetime.now(timezone.utc)
        user_p.save()

    urlflip = 'https://www.flipkart.com/offers-store?otracker=nmenu_offer-zone'

    page = session.get(urlflip, verify=False).content
    soup = BeautifulSoup(page, "html.parser")
    item = soup.find_all("div", class_="_2kSfQ4")

    TopDealFlipkart.objects.all().delete()

    for i in item:
        title = i.find('div', class_="iUmrbN").get_text()
        link = i.find('a', class_="K6IBc-")['href']
        price = i.find('div', class_="BXlZdc").get_text()

        new_item = TopDealFlipkart()
        new_item.title = title
        new_item.url = "https://www.flipkart.com" + str(link)
        new_item.price = price
        new_item.save()

    deal_f = TopDealFlipkart.objects.all()
    context = {'deal_list': deal_f,}

    return render(request, "news/flipkartdeal.html", context)


def scrapeA(request):
    session = requests.Session()
    session.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    user_p = UserProfile.objects.filter(user=request.user).first()
    if user_p is not None:
        user_p.last_scrape = datetime.now(timezone.utc)
        user_p.save()

    urlama = 'https://www.amazon.in/gp/goldbox?ref_=nav_cs_gb'

    page = session.get(urlama, verify=False).content
    soup = BeautifulSoup(page, "html.parser")
    item = soup.find_all("div", class_="_2kSfQ4")

    TopDealAmazon.objects.all().delete()

    for i in item:
        title = i.find('div', class_="iUmrbN").get_text()
        link = i.find('a', class_="K6IBc-")['href']
        price = i.find('div', class_="BXlZdc").get_text()

        new_item = TopDealAmazon()
        new_item.title = title
        new_item.url = "https://www.flipkart.com" + str(link)
        new_item.price = price
        new_item.save()


    deal_f = TopDealAmazon.objects.all()
    context = {'deal_list': deal_f}

    return render(request, "news/amazondeal.html", context)


def view_home(request):
    user_p = UserProfile.objects.filter(user=request.user).first()
    now = datetime.now(timezone.utc)
    time_difference = now - user_p.last_scrape
    time_diff_in_hr = time_difference/timedelta(minutes=60)
    next_scrape = 24 - time_diff_in_hr

    if time_diff_in_hr <= 12:
        hide = True
    else:
        hide = False

    context = {'hide': hide,
               'next_scrape': math.ceil(next_scrape)}

    return render(request, "news/home.html", context)
