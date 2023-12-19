<<<<<<< Updated upstream:achievement2/sources/app.py
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Подключение к базе данных PostgreSQL
# conn = psycopg2.connect(dbname='studydb', user='postgres', password='1995', host='localhost', port='5432')

@app.route('/')
def hello_world():
    return "Hello world!"

# @app.route('/', methods=['POST'])
# def process_number():
#     number = int(request.form.get('number'))
#
#     try:
#         # Проверка, если число уже обрабатывалось
#         if is_number_processed(number):
#             return jsonify({'error': 'Number has already been processed.'}), 400
#
#         # Проверка, если полученное число на единицу меньше уже обработанного числа
#         if is_number_less_than_previous(number):
#             return jsonify({'error': 'Number is less than the previous processed number.'}), 400
#
#         # Увеличение числа на единицу
#         processed_number = number + 1
#
#         # Сохранение числа в базе данных
#         save_number(processed_number)
#
#         return jsonify({'processed_number': processed_number})
#
#     except Exception as e:
#         # Обработка исключительных ситуаций
#         return jsonify({'error': str(e)}), 500
#
# def is_number_processed(number):
#     # Проверка наличия числа в базе данных
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM numbers WHERE value = %s", (number,))
#     result = cur.fetchone()
#     cur.close()
#     return result is not None
#
# def is_number_less_than_previous(number):
#     # Получение последнего обработанного числа из базы данных
#     cur = conn.cursor()
#     cur.execute("SELECT MAX(value) FROM numbers")
#     previous_number = cur.fetchone()[0]
#     cur.close()
#     return previous_number is not None and number < previous_number
#
# def save_number(number):
#     # Сохранение числа в базе данных
#     cur = conn.cursor()
#     cur.execute("INSERT INTO numbers (value) VALUES (%s)", (number,))
#     conn.commit()
#     cur.close()

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=5000)
=======
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Подключение к базе данных PostgreSQL
# conn = psycopg2.connect(dbname='studydb', user='postgres', password='1995', host='localhost', port='5432')

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/', methods=['POST'])
def process_number():
    number = int(request.form.get('number'))

    try:
        # Проверка, если число уже обрабатывалось
        if is_number_processed(number):
            return jsonify({'error': 'Number has already been processed.'}), 400

        # Проверка, если полученное число на единицу меньше уже обработанного числа
        if is_number_less_than_previous(number):
            return jsonify({'error': 'Number is less than the previous processed number.'}), 400

        # Увеличение числа на единицу
        processed_number = number + 1

        # Сохранение числа в базе данных
        save_number(processed_number)

        return jsonify({'processed_number': processed_number})

    except Exception as e:
        # Обработка исключительных ситуаций
        return jsonify({'error': str(e)}), 500

def is_number_processed(number):
    # Проверка наличия числа в базе данных
    cur = conn.cursor()
    cur.execute("SELECT * FROM numbers WHERE value = %s", (number,))
    result = cur.fetchone()
    cur.close()
    return result is not None

def is_number_less_than_previous(number):
    # Получение последнего обработанного числа из базы данных
    cur = conn.cursor()
    cur.execute("SELECT MAX(value) FROM numbers")
    previous_number = cur.fetchone()[0]
    cur.close()
    return previous_number is not None and number < previous_number

def save_number(number):
    # Сохранение числа в базе данных
    cur = conn.cursor()
    cur.execute("INSERT INTO numbers (value) VALUES (%s)", (number,))
    conn.commit()
    cur.close()

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=5000)
>>>>>>> Stashed changes:sources/app.py
