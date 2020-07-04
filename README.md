# Интерактивная карта Москвы

Карта Москвы с интересными местами.


## Пример
[Пример сайта](http://neverdieone.pythonanywhere.com/map)

[Админка на сайте](http://neverdieone.pythonanywhere.com/admin)

Данные для входа в админке:
* Login: `admin`
* Password: `adminadmin`

## Хочешь такой же?

1. Скачать репозиторий
    * `git clone https://github.com/NeverDieOne/django-afisha.git`
2. В корне проекта создать файл `.env`
    * Положить внутрь переменную `SECRET_KEY`
3. Установить зависимости
    * `pip install -r requirements.txt`
4. Сделать миграции
    * `python manage.py migrate`
5. Создать суперпользователя
    * `python manage.py createsuperuser`
6. Запустить сайт и наслаждаться
    * `python manage.py runserver` (команда не подходит для запуска на боевом сервере, см. ниже)
    
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).


## Запуск на боевом сервере

Гайд по деплою проекта Django на боевом сервере [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04).
