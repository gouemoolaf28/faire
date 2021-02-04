from database import cursor, db
import mysql.connector
# from app import brandView

def add_brand(id, name, country):
    try:
        sql = ("INSERT INTO faire_brand (id, name, country) VALUES (%s, %s, %s)")
        cursor.execute(sql, (id, name, country))
        db.commit()
    except mysql.connector.errors.IntegrityError:
        return
    # brand_id = cursor.lastrowid
    # print("Added brand {}". format(brand_id))

# for brand in brandView:
#     add_brand(brand['brand_id'], brand['name'], brand['country'])

    # print(brand['brand_id'])