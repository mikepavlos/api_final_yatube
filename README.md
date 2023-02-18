# api_final_yatube
### Описание
**API для YaTube**, социальной сети блогеров.  
Осуществляет взаимосвязь между клиентами и сервером по обработке стандартных запросов на: 
- вывод, создание, редактирование, удаление 
  - публикаций, 
  - комментариев к публикациям, 
- вывод информации о сообществах, 
- подписку на авторов публикаций.

Работа с API доступна аутентифицированным пользователям.  
Удалять и изменять пользователи могут только свой контент, чужой - только читать.  
Анонимным пользователям доступны запросы только на чтение, кроме доступа к контенту подписок.

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
venv\scripts\activate
```

Установить зависимости из файла requirements.txt:
```
py -m pip install --upgrade pip
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
Страница документации API будет доступна по адресу <http://127.0.0.1:8000/redoc>

---

### Примеры запросов
###### Получение списка публикаций    
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

###### Создание, изменение публикации
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
###### Получение публикации (либо ответ после создания/изменения)
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

###### Получение списка комментариев одной публикации
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

###### Создание комментария к публикации
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

###### Пример удаления
```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

---

###### Получение списка сообществ
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

###### Получение всех подписок пользователя, сделавшего запрос
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

###### Подписка пользователем на другого - автора публикаций
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

###### Создание токена для авторизованного пользователя
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

#### Автор
<sup>Михаил Павлов pavlovichmihaylovich@yandex.ru</sup>
