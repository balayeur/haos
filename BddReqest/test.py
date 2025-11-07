import requests
import json
from datetime import datetime, timedelta
from config import CONFIG

url = CONFIG['ha_url'] + "/api/history/period"
token = CONFIG['ha_token']

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

params = {
    "filter_entity_id": "sensor.burnerroom_boiler_temperature",
    "start_time": "2025-11-05T00:00:00+00:00",  # Убедитесь, что это правильная дата
    "end_time": "2025-11-05T23:59:59+00:00",
    "minimal_response": "true"
}

try:
    print(f"Отправка запроса к: {url}")
    print(f"Параметры: {params}")
    
    response = requests.get(url, headers=headers, params=params)
    print(f"HTTP статус: {response.status_code}")
    
    response.raise_for_status()
    data = response.json()
    
    print(f"Получено записей: {len(data[0]) if data and len(data) > 0 else 0}")
    
    # Безопасная обработка данных
    if data and len(data) > 0:
        valid_records = 0
        error_records = 0
        
        for i, entry in enumerate(data[0]):
            try:
                # Безопасное извлечение данных с значениями по умолчанию
                state = entry.get('state', None)
                last_updated = entry.get('last_updated', entry.get('last_changed', None))
                
                if state is not None and last_updated is not None:
                    print(f"{i+1:4d}. {last_updated}: {state}°C")
                    valid_records += 1
                else:
                    print(f"{i+1:4d}. [Пропущена запись с неполными данными]")
                    error_records += 1
                    
            except Exception as e:
                print(f"{i+1:4d}. [Ошибка обработки]: {e}")
                error_records += 1
        
        print(f"\n--- Статистика ---")
        print(f"Успешно обработано: {valid_records}")
        print(f"Пропущено записей: {error_records}")
        
    else:
        print("Нет данных")
        
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Общая ошибка: {e}")


# # Исправьте даты на те, за которые у вас точно есть данные
# params = {
#     "filter_entity_id": "sensor.burnerroom_boiler_temperature",
#     # "start_time": "2025-11-05T00:00:00+00:00",  # Убедитесь, что это правильная дата
#     # "end_time": "2025-11-05T23:59:59+00:00",
#     "minimal_response": "true"
#     # ,
#     # "no_attributes": "true"
# }

# try:
#     print(f"Отправка запроса к: {url}")
#     print(f"Параметры: {params}")
    
#     response = requests.get(url, headers=headers, params=params)
#     print(f"HTTP статус: {response.status_code}")
    
#     response.raise_for_status()
#     data = response.json()
    
#     print(f"Получено записей: {len(data[0]) if data and len(data) > 0 else 0}")

#     # Просто для диагностики - посмотрим на первые несколько записей
#     if data and len(data) > 0:
#         print("Первые 5 записей (сырые данные):")
#         for i, entry in enumerate(data[0][:5]):
#             print(f"{i+1}. {json.dumps(entry, indent=2, ensure_ascii=False)}")
#             print("---")
    
#     # # Безопасный перебор данных
#     # if data and len(data) > 0:
#     #     for entry in data[0]:
#     #         print(f"{entry['last_updated']}: {entry['state']}")
#     # else:
#     #     print("Нет данных за указанный период")
        
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: {e}")
# except Exception as e:
#     print(f"Общая ошибка: {e}")


# # Параметры запроса
# params = {
#     "filter_entity_id": "sensor.burnerroom_boiler_temperature",
#     "start_time": "2025-11-05T00:00:00+00:00",  # Начальная дата (в UTC)
#     "end_time": "2025-11-05T23:59:59+00:00",    # Конечная дата (в UTC)
#     "minimal_response": "true" # Возвращает только необходимые данные, уменьшая объем
# }

# try:
#     response = requests.get(url, headers=headers, params=params)
#     response.raise_for_status()  # Проверяем на ошибки HTTP
#     data = response.json()
#     print(data)
#     # Данные возвращаются в виде списка списков для каждого entity_id
#     for entry in data[0]:
#         print(f"{entry['last_updated']}: {entry['state']}")
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: {e}")