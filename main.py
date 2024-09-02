import sqlite3

def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

   
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    connection.close()

if __name__ == "__main__":
    main()
