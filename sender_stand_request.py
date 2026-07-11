# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data
# Создаём заказ через API и возвращает его трек-номер
def create_order():
    # Формируем полный URL для создания заказа: базовый адрес + путь к эндпоинту
    url_create = configuration.URL_SERVICE + configuration.CREATE_PATH
    # Отправляем POST-запрос с данными заказа (из data.order_body) на полученный URL
    resp_create = requests.post(url_create, json=data.order_body)
    # Извлекаем трек-номер из JSON-ответа сервера и приводим его к строке
    return str(resp_create.json()["track"])
   

# Получаем данные заказа по трек-номеру через API
def get_order_by_track(track):
    # Формируем URL для получения данных заказа по треку
    url_get = configuration.URL_SERVICE + configuration.GET_BY_TRACK_PATH
    # Отправляем GET-запрос, передавая трек-номер в параметрах запроса.
    resp_get = requests.get(url_get,
                            params={configuration.TRACK_PARAM_NAME: track}
                            )
    # Возвращаем JSON-ответ сервера, чтобы дальше проверить данные заказа
    return resp_get





