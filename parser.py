import requests

def get_weather_no_key(city_coords):
    """
    Запрашивает погоду через Open-Meteo (без API ключа!)
    """
    # URL бесплатного API Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Параметры: широта, долгота и запрос текущей погоды
    params = {
        'latitude': city_coords['lat'],
        'longitude': city_coords['lon'],
        'current_weather': 'true'
    }

    try:
        print(f"Загружаю погоду для координат {city_coords['lat']}, {city_coords['lon']}...")
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Извлекаем данные из JSON
        weather = data['current_weather']
        temperature = weather['temperature']
        wind_speed = weather['windspeed']
        
        # Коды погоды WMO (упрощенно)
        weather_code = weather['weathercode']
        weather_desc = get_weather_description(weather_code)
        
        print("-" * 30)
        print(f"🌡 Температура: {temperature}°C")
        print(f"☁️ Состояние: {weather_desc}")
        print(f"💨 Скорость ветра: {wind_speed} км/ч")
        print("-" * 30)

    except Exception as err:
        print(f"❌ Ошибка: {err}")

def get_weather_description(code):
    """Простой расшифровщик кодов погоды WMO"""
    codes = {
        0: "Ясно",
        1, 2, 3: "Переменная облачность",
        45, 48: "Туман",
        51, 53, 55: "Морось",
        61, 63, 65: "Дождь",
        71, 73, 75: "Снег",
        95, 96, 99: "Гроза"
    }
    # Ищем описание, если точного кода нет, берем ближайшее или "Неизвестно"
    for key, value in codes.items():
        if isinstance(key, tuple) and code in key:
            return value
        if key == code:
            return value
    return "Неизвестно"

if __name__ == "__main__":
    print("=== Парсер погоды (БЕЗ API ключа!) ===")
    
    # Словарь с координатами популярных городов
    cities = {
        "москва": {"lat": 55.75, "lon": 37.62},
        "санкт-петербург": {"lat": 59.93, "lon": 30.33},
        "лондон": {"lat": 51.50, "lon": -0.12},
        "нью-йорк": {"lat": 40.71, "lon": -74.00}
    }
    
    user_city = input("Введите город (Москва, Санкт-Петербург, Лондон, Нью-Йорк): ").strip().lower()
    
    if user_city in cities:
        get_weather_no_key(cities[user_city])
    else:
        print("❌ Город не найден в базе. Попробуйте один из предложенных.")