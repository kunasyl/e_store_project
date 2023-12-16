## E-Store Project
**E-Store Project** - REST API приложение онлайн магазина, написанный на Django Rest Framework.

### Структура:
Приложение состоит из:
- `users` - содержит функционал JWT авторизации/регистрации
- `products` - содержит модели товаров
- `orders` - содержит функционал добавления/обновления заказа
- `utils` - содержит функции для операций создания, сохранения, взятия данных из БД

### Установка
Проект написан на django rest framework.

В `requirements.txt` указаны все нужные пакеты.

### Использование
Для создания пользователя отправьте POST запрос на `users/create/`:
```JSON
{
    "email": "hello@mail.ru",
    "username": "hello",
    "password": "hello123"
}
```

Для получения token отправьте POST запрос на `users/token/` с данными пользователя.

Просмотр товаров доступен по ссылке `products/`.

Для просмотра заказов пользователя отправьте POST запрос с access токеном пользователя в `orders/`

Для создания заказа отправьте POST запрос с access токеном пользователя в `orders/`:
```JSON
{
    "user_id": 2,
    "status": "Не заказано",
    "order_items": [
        {
            "order_id": "b18e5c1c-5acf-4927-afe4-86f0558de7aa",
            "product_id": "245f16e1-89c3-4dc9-834f-af49057ecccc",
            "product_count": 2,
            "product_price": 999
        }
    ]
}
```