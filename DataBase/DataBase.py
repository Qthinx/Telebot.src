import sqlite3

# Підключаємо базу даних
conn = sqlite3.connect('Database/database.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_nickname: str, user_status: str, user_balance: int, user_last_activity: str):
    cursor.execute('SELECT user_id, user_last_activity FROM Db WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result is None:
        # Виконати додаткові дії для збереження значення user_nickname
        cursor.execute('INSERT INTO Db (user_id, user_name, user_nickname, user_status, user_balance, user_last_activity) VALUES (?, ?, ?, ?, ?, ?)', (user_id, user_name, user_nickname, user_status, user_balance, user_last_activity))
    else:
        previous_last_activity = result[1]
        new_last_activity = previous_last_activity + '\n' + user_last_activity
        cursor.execute('UPDATE Db SET user_name = ?, user_nickname = ?, user_status = ?, user_balance = ?, user_last_activity = ? WHERE user_id = ?', (user_name, user_nickname, user_status, user_balance, new_last_activity, user_id))
    conn.commit()
