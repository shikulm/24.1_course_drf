# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /code

# Копируем зависимости в контейнер
COPY ./requirements.txt /code/

# Устанавливаем зависимости
RUN apt-get update
RUN pip install -r requirements.txt

# Копируем код приложения в контейнер
copy . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]

#systemctl start docker



