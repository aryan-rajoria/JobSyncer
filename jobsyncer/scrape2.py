import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from bs4.element import Tag
import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

config = load_config('config.json')

def extract_text_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(separator=' ', strip=True)
        lines = (line.strip() for line in text.splitlines())
        text = ' '.join(line for line in lines if line)

        return text

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return ""

url = config['url2']
text_content = extract_text_content(url)
print(text_content)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)
