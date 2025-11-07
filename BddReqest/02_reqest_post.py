import requests
import json
from config import CONFIG

url = CONFIG['ha_url'] + "/api/history/period"
token = CONFIG['ha_token']
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}


# Данные в теле запроса
data = {
    "filter_entity_id": "sensor.burnerroom_boiler_temperature",
    "start_time": "2023-12-01T00:00:00+00:00",
    "end_time": "2023-12-01T23:59:59+00:00",
    "minimal_response": True
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("Успех!")
        for entry in result[0]:
            print(f"{entry['last_updated']}: {entry['state']}")
    else:
        print(f"Ошибка: {response.text}")
        
except Exception as e:
    print(f"Ошибка: {e}")