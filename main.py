from database import cursor, db
import mysql.connector

def add_brand(id, name, country):
    try:
        sql = ("INSERT INTO faire_brand (id, name, country) VALUES (%s, %s, %s)")
        cursor.execute(sql, (id, name, country))
        db.commit()
    except mysql.connector.errors.IntegrityError:
        return