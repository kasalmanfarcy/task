from flask import Flask
import sqlite3

app = Flask(__name__)

def collectData():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    
    
    data = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in rows]
    
    connection.close()
    
    return data

@app.route('/users', methods=['GET'])
def getUsers():
    data = collectData()
    
   
    output = ""
    for user in data:
        output += f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}\n"
    
    return output

if __name__ == "__main__":
    app.run(debug=True)
