import sqlite3


def get_db_connection():
    """Функция для удобного подключения к базе данных"""
    return sqlite3.connect('user_info.db', check_same_thread=False)


def user_exist(user_id):
    """Проверка есть ли пользователь с определенным id в базе данных"""
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (user_id,))
    count = cursor.fetchone()[0]
    connect.close()
    return count


def add_user(user_id, send_question=0):
    """Добавление нового пользователя в базу данных"""
    conn = get_db_connection()
    cur = conn.cursor()
    if not user_exist(user_id):
        cur.execute('INSERT INTO users (user_id, send_question) VALUES (?, ?)',
                    (user_id, send_question,))
    conn.commit()
    conn.close()


def set_send_question(user_id, send_question):
    """Изменение начала/конца создания конспекта"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE users SET send_question = ? WHERE user_id = ?',
                (send_question, user_id,))
    conn.commit()
    conn.close()


def get_send_question(user_id):
    """Получение значения состояния создания конспекта у определенного пользователя"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT send_question FROM users WHERE user_id = ?', (user_id,))
    result = cur.fetchone()
    conn.close()
    return result[0]
