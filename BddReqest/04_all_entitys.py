import requests
import json
from config import CONFIG

url = CONFIG['ha_url'] + "/api/states"
token = CONFIG['ha_token']

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    print(f"Всего entities: {len(data)}")
    print("\nВсе датчики (sensor.*):")
    print("-" * 50)
    
    sensors = [entity for entity in data if entity['entity_id'].startswith('sensor.')]
    
    for sensor in sensors:
        entity_id = sensor['entity_id']
        name = sensor['attributes'].get('friendly_name', 'No name')
        state = sensor['state']
        unit = sensor['attributes'].get('unit_of_measurement', '')
        print(f"{entity_id:50} | {name:50} | {state:20} {unit}")
    
    print(f"\nВсего датчиков: {len(sensors)}")
    
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")