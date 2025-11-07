import requests



try:
    response = requests.get(url, headers=headers)
    print(f"Status Code для сенсора: {response.status_code}")
    if response.status_code == 200:
        sensor_data = response.json()
        print(f"Сенсор существует: {sensor_data}")
    else:
        print("Сенсор не найден! Проверьте название.")
        
except Exception as e:
    print(f"Ошибка: {e}")