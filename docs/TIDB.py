pip install mysql-connector-python
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector  # or import pymysql

app = Flask(__name__)

# Establish a connection to TiDB
def get_db_connection():
    connection = mysql.connector.connect(
        host='your_tidb_host',
        port=4000,  # default TiDB port
        user='your_username',
        password='your_password',
        database='your_database_name'
    )
    return connection

@app.route('/submit_query', methods=['POST'])
def submit_query():
    query = request.form['query']  # The SQL query entered by the user

    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('output.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
