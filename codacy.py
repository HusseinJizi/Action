
import sqlite3

def connect_db():
    conn = sqlite3.connect("database.db")
    return conn, conn.cursor()

def get_user_data(user_id):
    # 🚨 SQL-Injection möglich, da user_id direkt eingefügt wird!
    conn, cursor = connect_db()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

def calculate_discount(price, discount):
    # 🚨 Kein Typ-Check: Wenn price oder discount keine Zahl ist, gibt es einen Fehler!
    return price - (price * discount / 100)

# 🚨 Unbenutzte Variable (Codacy warnt vor toten Code)
unused_variable = "Ich werde nicht genutzt!"

def print_data():
    data = get_user_data(1)
    for d in data:
        print("User:", d)  # 🚨 print() anstatt Logging (Codacy empfiehlt Logging)

def main():
    price = 100
    discount = "20"  # 🚨 Falscher Datentyp! String statt Zahl
    final_price = calculate_discount(price, discount)  # Fehler beim Rechnen
    print("Final Price:", final_price)  # 🚨 print() anstatt Logging

if __name__ == "__main__":
    main()
