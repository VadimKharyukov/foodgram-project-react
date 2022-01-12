# yamdb_final
![yamdb_final](https://github.com/VadimKharyukov/yamdb_final/actions/workflows/main.yml/badge.svg)

Это учебно-практический проект студента ЯндексПрактикума направления бекэнд
 разработки.Цель проекта создание API для социальной сети Yatube.Проект интегрирован в Docker.
***
####Возможности:
* Создавать посты и редактировать посты
* Добавлять к постам картинки и комментарии
* Отслеживать интересющего вас пользователя
* Просто общаться

### Как запустить проект:


```
https://github.com/VadimKharyukov/yamdb_final.git
```
### Как установить проект:
1. Установка Docker, docker-compose можно найти в официальной статье.
2. Заполнить фаил окружения .env из template файла в той же директории.
3. Собрать и запустить контейнер.
```
docker-compose up -d --build
```
4.Миграции.

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
5. Сбор статитики.
```
docker-compose exec web python manage.py collectstatic --no-input
```
6. Admin сайта и redoc.
```
62.84.114.36/redoc/
62.84.114.36/admin/
```

Для добавления нового пользователя нужно отправить POST-запрос с параметрами email и username на эндпоинт 

```
/api/v1/auth/signup/
```
Сервис YaMDB отправляет письмо с кодом подтверждения на указанный адрес email.

Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт: 

```
/api/v1/auth/token/
```
В ответе на запрос ему приходит token. Введя его в соответствующее поле можете пользоваться сервисом!
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт:
```
/api/v1/users/me/
```
И заполнить поля в своём профайле.
Примеры запросов сервиса:
```
/api/v1/categories/ - категории
/api/v1/genres/ - жанры
/api/v1/titles/ - списки воспроизведения
/api/v1/titles/{title_id}/reviews/ - отзывы
/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - комментарии
/api/v1/users/ - пользователи

```