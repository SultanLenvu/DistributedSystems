from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Подключение к базе данных Postgres через переменные окружения
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# db_host = 'postgres-container'
# db_port = '5432'
# db_name = 'testdb'
# db_user = 'sultan'
# db_password = 'lenvu'

# Создание таблицы при запуске приложения
conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS numbers (value INTEGER PRIMARY KEY)')
conn.commit()
cur.close()
conn.close()


@app.route('/', methods=['POST'])
def process_number():
    number = request.json.get('number')

    # Проверка, что число не было обработано ранее
    conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
    )
    cur = conn.cursor()
    cur.execute('SELECT value FROM numbers WHERE value = %s', (number,))
    existing_number = cur.fetchone()
    if existing_number:
        cur.close()
        conn.close()
        error_message = 'Число уже обработано'
        app.logger.error(error_message)
        return jsonify({'error': error_message}), 400

    # Проверка, что число на единицу больше предыдущего обработанного числа
    cur.execute('SELECT value FROM numbers ORDER BY value DESC LIMIT 1')
    previous_number = cur.fetchone()
    if previous_number and number != previous_number[0] + 1:
        cur.close()
        conn.close()
        error_message = 'Нарушена последовательность чисел'
        app.logger.error(error_message)
        return jsonify({'error': error_message}), 400

    # Сохранение числа в базе данных
    cur.execute('INSERT INTO numbers (value) VALUES (%s)', (number,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'result': number + 1})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
