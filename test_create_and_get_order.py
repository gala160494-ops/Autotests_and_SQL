# СЕРГЕЙ ГАЛКИН, 44-я КОГОРТА - ФИНАЛЬНЫЙ ПРОЕКТ. ИНЖЕНЕР ПО ТЕСТИРОВАНИЮ ПЛЮС
# Подключаем файл с функциями для работы с API (создание и получение заказа)
import sender_stand_request

# Тест: создаём заказ и проверяем, что можем получить его по трек-номеру
def test_create_and_get_order():
    # Создаём заказ — получаем трек-номер
    track = sender_stand_request.create_order()
    # По треку запрашиваем данные о заказе
    response = sender_stand_request.get_order_by_track(track)
    # Проверяем, что запрос прошёл успешно (статус 200)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"