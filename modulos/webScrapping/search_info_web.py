import requests
from bs4 import BeautifulSoup

def obtener_info_web(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string
