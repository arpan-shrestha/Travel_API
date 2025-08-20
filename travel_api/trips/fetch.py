import requests
import re
from bs4 import BeautifulSoup
from .models import Trip, Activities

def fetch_trips():
    urls = [
        "https://www.antholidays.com/destination-international",
        "https://www.antholidays.com/destination-domestic"]
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')

        cards = soup.select('div.hover\\:shadow-lg.border')
        for card in cards:
            title = card.find('h2').text.strip()

            duration_tag = card.select_one('div.text-gray-500.text-sm span.text-black')
            duration_text = duration_tag.text.strip() if duration_tag else ""

            duration_match = re.search(r'(\d+)\s*Days?', duration_text, re.IGNORECASE)
            duration = int(duration_match.group(1)) if duration_match else 0

            night_match = re.search(r'(\d+)\s*Nights?', duration_text, re.IGNORECASE)
            night = int(night_match.group(1)) if night_match else 0

            difficulty_tag = card.select('div span.text-black')
            difficulty = difficulty_tag[1].text.strip() if len(difficulty_tag) > 1 else "Unknown"

            trip_url = "https://www.antholidays.com" + card.find('a')['href']


            Trip.objects.update_or_create(
                url=trip_url,
                defaults={
                    'title':title,
                    'duration':duration,
                    'night':night,
                    'difficulty':difficulty
                }
            )

def fetch_activities():
    url = "https://www.antholidays.com/activities"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    cards = soup.select('div.hover\\:shadow-lg.border')
    for card in cards:
        title = card.find('h2').text.strip()
        activity_url = "https://www.antholidays.com" + card.find('a')['href']
        
        Activities.objects.update_or_create(
            url = activity_url,
            defaults={
                'title':title
            }
        )