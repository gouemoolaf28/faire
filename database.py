import mysql.connector

config = {
    'user': 'doadmin',
    'password': 'ycse5bf3s4bvrc10',
    'host': 'db-mysql-nyc1-47005-do-user-8592501-0.b.db.ondigitalocean.com',
    'database': 'fairedb',
    'port':25060
}

db = mysql.connector.connect(**config)
cursor = db.cursor()