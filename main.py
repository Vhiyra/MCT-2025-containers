from flask import Flask, request
import pcycopg2

app = Flask(__name__)

@app.route('/')
def dataBase():
    conn = psycopg2.connect(
        host='<host>'
        database='<db>'
        user='<user>'
        password='<123>'
    )
    return conn
    
    
@app.route('/ping')
def ping():
    ip = request.remote_addr
    conn = dataBase()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO visits (ip) VALUES (%s)", (ip,))
    conn.commit()
    cursor.close()
    conn.close()
    return "pong\n"
    
def visits():
    conn = dataBase()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM visits")
    t = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return str(t) + '\n'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
