import requests
from datetime import datetime



# Параметры в теле запроса (иногда требуется)
params = {
    "filter_entity_id": "sensor.burnerroom_boiler_temperature",
    "start_time": "2023-12-01T00:00:00+00:00",
    "end_time": "2023-12-01T23:59:59+00:00",
    "minimal_response": "true"
}

try:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    
    if response.status_code == 200:
        data = response.json()
        print("Успех! Данные получены:")
        for entry in data[0]:
            print(f"{entry['last_updated']}: {entry['state']}")
    else:
        print(f"Ошибка: {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")