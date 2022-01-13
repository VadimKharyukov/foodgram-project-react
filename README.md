# Diplom project
![foodgram-project-react](https://github.com/VadimKharyukov/foodgram-project-react/actions/workflows/main.yml/badge.svg)

Дипломный проект курса Python-разработчик Яндекс-Практикум
***
####Возможности:
сайт Foodgram, «Продуктовый помощник» на этом сервисе пользователи смогут публиковать рецепты,
подписываться на публикации других пользователей, 
добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов,
необходимых для приготовления одного или нескольких выбранных блюд.

### Как запустить проект:


```
https://github.com/VadimKharyukov/foodgram-project-react.git
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
7. Более подробная информация доступна
```
62.84.114.36/api/docs/
```