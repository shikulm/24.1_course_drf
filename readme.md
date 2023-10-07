Приложение используется для работы с курсами и уроками. Доступ к моделям (CRUD) осуществляется через API.
Для тестирования работы эндпоинтов рекомендуется использовать Postman.

Структура моделей приложения:

Пользователь:
- email;
- телефон;
- город;
- аватарка.

Курс:
- название,
- превью (картинка),
- описание.

Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

<h3> Для использования Docker compose выполните следующие действия: </h3>

- Запустите службу docker (в терминале для Ubuntu можно выполнить команду): 

> sudo service docker start

- Собрать Docker-образ

> docker-compose build

- Поднять Docker-образ

> docker-compose up
 
- При необходимости создать БД

> docker-compose exec db psql -U postgres
> 
> create database course_drf
> 
> \q


<h3> Для использования Docker выполните следующие действия: </h3>

- Запустите службу docker (в терминале для Ubuntu можно выполнить команду): 

> sudo service docker start

- Собрать Docker-образ с проектом (если изменится содержимое проекта и используемые библиотеки)

> docker build -t course_drf .
Здесь -t course_drf задает имя образа, а . указывает на текущую директорию с Dockerfile.

- Запустить контейнер с помощью команды:

> docker run course_drf 
 

<h3> Перед выполнением проекта в Ubuntu выполните команды </h3>

> sudo service postgresql start

> sudo service redis-server start 

<h3> В терминале выполняем команды для начала работы </h3>

Установка библиотек:
> python -m pip install -r requirement.txt

Активация среды окружения (для Linux):
> source env/bin/activate 

Запуск сервера:
>  python manage.py runserver

<h3> В процессе работы могут потребоваться команды </h3>

Фиксация изменений в git
>git commit -a -m ' '

Запуск отложенных задач celery (с декоратором @shared_task)
>celery -A conf worker -l INFO 
 
Запуск периодических задач celery (с декоратором @shared_task)
> celery -A conf beat -l INFO -S django --logfile=celery.log

или
> celery -A conf beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler