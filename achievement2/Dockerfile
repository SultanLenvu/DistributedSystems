FROM ubuntu:latest

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libpq-dev

# Установка Flask и psycopg2
RUN pip3 install flask psycopg2

# Копирование приложения в контейнер
WORKDIR /work
COPY sources /work

# Установка зависимостей
RUN pip3 install -r requirements.txt

# Установка переменных окружения
ENV DB_HOST=postgres-container
ENV DB_PORT=5432
ENV DB_NAME=testdb
ENV DB_USER=sultan
ENV DB_PASSWORD=lenvu

EXPOSE 5000

# Запуск приложения
CMD ["python3", "app.py"]

