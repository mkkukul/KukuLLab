import requests
from bs4 import BeautifulSoup
url = requests.get("")
if url.status_code