from flask import Flask
import psycopg2

from os import environ

app = Flask(__name__)


try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print "I am unable to connect to the database"


@app.route('/')
def hello_world():
    return 'REST API'


if __name__ == '__main__':
    port = environ.get('APP_PORT', '5000')
    port = int(port)
    app.run(debug=True, host='0.0.0.0', port=port)