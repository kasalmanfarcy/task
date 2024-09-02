import sqlite3

def getInput():
    name = input("Enter name: ")
    email = input("Enter email: ")
    return (name, email)

def main():
  
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    
    totalRow = int(input("How many users would you like to add? "))
    for _ in range(totalRow):
        userData = getInput()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', userData)

    
    conn.commit()
    conn.close()

    print("Table created and data inserted successfully.")

if __name__ == "__main__":
    main()
