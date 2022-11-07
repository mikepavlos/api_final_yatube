# api_final_yatube
### Описание
API для Yatube, социальной сети блогеров.
Осуществляет взаимосвязь между клиентами и сервером по обработке стандартных запросов на: 
- вывод, создание, редактирование, удаление публикаций, 
- вывод, создание, редактирование, удаление комментариев к публикациям, 
- вывод информации о сообществах, 
- подписку на авторов публикаций.
### Технологии
- Python 3.7
- Django 2.2
- DRF 3.12
- SimpleJWT 4.7
### Установка и запуск проекта в dev-режиме (Windows)
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/mikepavlos/api_final_yatube.git
```
Создать и активировать виртуальное окружение:
```
py -m venv venv
```
```
venv\scripts\activate
```

Установить зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
py manage.py migrate
```
Запустить проект:
```
py manage.py runserver
```
Страница документации API будет доступна по адресу (http://127.0.0.1:8000/redoc)

---
### Примеры запросов
```
GET /api/v1/posts/
```
Ответ
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
---
```
POST /api/v1/posts/
PUT (PUTCH) /api/v1/posts/{id}/
```
Запрос
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
```
GET /api/v1/posts/{id}/
```
Ответ
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
---
```
GET /api/v1/posts/{post_id}/comments/
```
Ответ
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
---
```
POST /api/v1/posts/{post_id}/comments/
```
Запрос
```json
{
  "text": "string"
}
```
---
```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```
---
```
GET /api/v1/groups/
```
Ответ
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
---
```
GET /api/v1/follow/
```
Ответ
```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```
---
```
POST /api/v1/follow/
```
Запрос
```json
{
  "following": "string"
}
```
Ответ
```json
{
  "user": "string",
  "following": "string"
}
```
---
```
POST /api/v1/jwt/create/
```
Запрос
```json
{
  "username": "string",
  "password": "string"
}
```
---

### Автор
Михаил Павлов (Михалис)