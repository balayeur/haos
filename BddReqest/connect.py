import requests
from config import CONFIG

base_url = CONFIG['ha_url'] + "/api/"
token = CONFIG['ha_token']

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# Проверяем доступность API
try:
    response = requests.get(f"{base_url}", headers=headers)
    print(f"API status: {response.status_code}")
    if response.status_code == 200:
        print("API доступен!")
        print(response.json())
except Exception as e:
    print(f"Ошибка: {e}")