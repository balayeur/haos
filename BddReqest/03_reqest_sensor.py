import requests
from config import CONFIG

url = CONFIG['ha_url'] + "/api/states/sensor.burnerroom_boiler_temperature"
token = CONFIG['ha_token']
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# url = "http://192.168.1.36:8123/api/states/sensor.burnerroom_boiler_temperature"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIzYWVhZGU0N2I2Y2Q0MTVmYThmYTE1MWJiMTQ4ZTRlYSIsImlhdCI6MTc2MjUyNDUzNiwiZXhwIjoyMDc3ODg0NTM2fQ.M6Ue9VoJDCKAGG57IDwLjyonRFOeI1frocJIQ9UsF4Y",
#     "Content-Type": "application/json",
# }

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