# Проект API_Final_YATUBE
## Описание проекта
#### Смысл данного проекта заключается в создании API интерфейса для социальной сети Yatube.
##### Функциаональные способности проекта:
* Осуществлять подписку на авторизованного пользователя и отписку от него.
* Авторизованный пользователь сможет просматривать посты, также создавать новые посты, удалять их и изменять.
* Просматривать сообщества.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.

#### К API для Yatube есть документация по адресу `http://localhost:8000/redoc/`
## Установка
Клонируем репозиторий на локальную машину:

``` git clone https://github.com/DumaDim/api_final_yatube.git```

Создаем виртуальное окружение:
 
``` python -m venv venv```
 
Устанавливаем зависимости:

``` pip install -r requirements.txt```

Создание и применение миграций:

``` python manage.py makemigrations``` и ``` python manage.py migrate```

Запускаем django сервер:

``` python manage.py runserver```

Все готово к использованию API!

## Примеры
Для ознакомления с функционалом проекта API для Yatube будет использована программа [Postman] (https://winter-astronaut-191968.postman.co/).

#### Получение токена

Отправляем POST-запрос на адрес ```api/v1/jwt/create/``` и передаем 2 поля в `data`.

1. `username` - указываем имя пользователя.
2. `password` - указываем пароль пользователя.

#### Создаем новый пост

Передаем POST-запрос на адрес ```api/v1/posts/``` и передаем обязательное поле `text`, в заголовке указываем `Authorization`:`Bearer <токен>`:

```json
{
    "text": 
        "Мой первый пост."
    
}
```

__Получаем ответ на данный запрос:__

```json
{
    "id": 2,
    "author": "Dmitrii",
    "text": "Мой первый пост.",
    "pub_date": "2022-04-22T12:00:22.021094Z",
    "image": null,
    "group": null
}
```

#### Оставляем комментарий к посту пользователя

Передаем POST-запрос на адрес ```api/v1/posts/{post_id}/comments/``` и передаем обязательные поля `post` и `text`, в заголовке указываем `Authorization`:`Bearer <токен>`:

```json
{
    "post": 
        1,
    "text": 
        "Тест" 
}
```

__Получаем ответ на данный запрос:__

```json
{
    "id": 1,
    "author": "Dmitrii",
    "text": "Тест",
    "created": "2022-04-22T12:06:13.146875Z",
    "post": 1
}
```