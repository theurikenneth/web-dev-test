import sqlite3
import flask
import requests
from flask import request, jsonify
import json

DATABASE_NAME = "ken_database"


import sqlite3
from flask import g


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    cur = get_db().cursor()


@app.route('/drivers', methods=['GET'])
def get_by_id():
    connection = get_db()
    cursor = connection.cursor()
    query = "SELECT count(distinct uuid) as count_of_hotels FROM hotels"
    result = cursor.execute(query)

    items = []
    for row in result:
        for key in cursor.description:
            items.append({key[0]: value for value in row})

    return(json.dumps({'items':items}))


# @app.route('/drivers', methods=['GET'])
# def get_by_id():
#     db = get_db()
#     cursor = db.cursor()
#     statement = "SELECT first_name, last_name FROM drivers"
#     cursor.execute(statement)
#     data = cursor.fetchall()
#     data_json = []
#     header = [i[0] for i in cursor.description]
#     for i in data:
#         data_json.append(dict(zip(header, i)))
#     return data_json


# @app.route('/all_drivers', methods=['GET'])
# def get_all():
#     db = get_db()
#     cursor = db.cursor()
#     statement ="""with drivers_trips as (SELECT distinct a.driver_id, a.hotel_id, a.start_time, a.delivery_time, a.rating, b.first_name, b.last_name 
#         FROM trips AS a left join drivers AS b
#         ON a.driver_id = b.uuid)
        
#         select * from drivers_trips
#       """
#     cursor.execute(statement)
#     data = cursor.fetchall()
#     data_json = []
#     header = [i[0] for i in cursor.description]
#     for i in data:
#         data_json.append(dict(zip(header, i)))
#     return data_json
    # return cursor.fetchmany()

# @app.route('/home', methods=['GET'])
# def get_all():
#     db = get_db()
#     cursor = db.cursor()
#     statement = """with drivers_trips as (SELECT distinct a.driver_id, a.hotel_id, a.start_time, a.delivery_time, a.rating, b.first_name, b.last_name 
#         FROM trips AS a left join drivers AS b
#         ON a.driver_id = b.uuid),

#         hotel_trips as (SELECT c.first_name, c.last_name, c.start_time, c.delivery_time, c.rating, d.name, d.address From drivers_trips AS C
#         LEFT JOIN hotels AS d
#         ON c.hotel_id = d.uuid) 
        
#         select * from hotel_trips where rating between 1 and 2
#         """
#     cursor.execute(statement)
#     return cursor.fetchall()




# Where start_time= and delivery_time=  and first_name= and last_name= and hotel = and rating between _  and _ 



app.run()