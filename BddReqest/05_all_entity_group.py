import requests
from collections import defaultdict
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
    
    # Группировка по domain (первая часть entity_id)
    domains = defaultdict(list)
    
    for entity in data:
        domain = entity['entity_id'].split('.')[0]
        domains[domain].append(entity['entity_id'])
    
    print("Статистика по типам устройств:")
    print("-" * 30)
    for domain, entities in sorted(domains.items()):
        print(f"{domain:15}: {len(entities):3} entities")
    
    # Подробно по датчикам
    if 'sensor' in domains:
        print(f"\nДетали по датчикам ({len(domains['sensor'])} шт.):")
        print("-" * 50)
        for sensor in sorted(domains['sensor']):
            print(f"  - {sensor}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")