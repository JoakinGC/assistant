import requests
from bs4 import BeautifulSoup
from googletrans import Translator

class WeatherScraper:
    def __init__(self, city):
        self.city = city.replace(" ", "-")
        self.base_url = f"https://www.weather-forecast.com/locations/{self.city}/forecasts/latest"
        self.translator = Translator()

    def get_weather(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            weather_div = soup.find('div', class_='b-forecast__table-days-name')
            weather_info = weather_div.find_next('span', class_='phrase').text

            
            translated_info = self.translator.translate(weather_info, src='en', dest='es').text
            return translated_info
        else:
            return None
        

