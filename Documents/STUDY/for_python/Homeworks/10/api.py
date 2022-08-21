import requests
from dateutil.parser import parse

# Получить курсы и время их обновления
def get_full_exchange_rates(orig_curr):
    url = f"https://open.er-api.com/v6/latest/{orig_curr}"
    # Запрос к обменнику через API с возвратом результата по курсам и времени  в виде json.
    data = requests.get(url).json()
    if data["result"] == "success":
        # Забрали время последнего обновления.
        exchange_rates = data["rates"]
    return exchange_rates

# Конвертация
def convert_currency(orig_curr, transf_curr, quantity):
    # Получили время обновления и курсы по заданным валютам.
    exchange_rates = get_full_exchange_rates(orig_curr)
    # Вывели время и нужный курс
    return round(exchange_rates[transf_curr] * quantity, 2)

# Время обновления.
def get_update_time():
    url = f"https://open.er-api.com/v6/latest/RUB"
    # Запрос к обменнику через API с возвратом результата по курсам и времени  в виде json.
    data = requests.get(url).json()
    if data["result"] == "success":
        # Забрали время последнего обновления.
        last_updated_datetime = parse(data["time_last_update_utc"]).strftime("%d.%m.%Y - %H:%M:%S")
    return last_updated_datetime