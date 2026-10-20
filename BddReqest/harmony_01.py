import requests
import json
from config import CONFIG

# url = CONFIG['ha_url'] + "/aapi/services/script/harmony_youtube_sequence"
# token = CONFIG['ha_token']
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json",
# }


HA_URL = CONFIG['ha_url']
ACCESS_TOKEN = CONFIG['ha_token']

def execute_ha_script(script_name, entity_id=None, data=None):
    """Запуск скрипта Home Assistant"""
    url = f"{HA_URL}/api/services/script/{script_name}"
    print (f"Выполняем скрипт по URL: {url}")
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {}
    if entity_id:
        payload["entity_id"] = entity_id
    if data:
        payload.update(data)
    
    try:
        # response = requests.post(url, headers=headers, timeout=10)
        # response.raise_for_status()
        # print(f"Скрипт '{script_name}' выполнен успешно")
        # return response.json()
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        print(f"Статус: {response.status_code}")
        
        if response.status_code == 200:
            print("✓ Успешно")
            return response.json()
        else:
            print(f"Ответ: {response.text}")
            return None
    except Exception as e:
        print(f"Ошибка выполнения скрипта: {e}")
        return None

# Если у вас есть скрипт harmony_youtube_sequence
execute_ha_script("all_in_one_youtube")


# curl -X POST \
#   -H "Authorization: Bearer YOUR_LONG_LIVED_ACCESS_TOKEN" \
#   -H "Content-Type: application/json" \
#   http://YOUR_HA_IP:8123/api/services/script/harmony_youtube_sequence    