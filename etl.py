import pandas as pd
from sqlalchemy import create_engine
import sqlite3

drivers = pd.read_json("files/drivers.json")
hotels = pd.read_json("files/hotels.json")
trips = pd.read_json("files/trips.json")

data = [drivers, hotels, trips]

# create database
conn = sqlite3.connect('ken_database')
cur = conn.cursor()

# Tables in the database
tables = ["drivers", "hotels", "trips"]
# Creating the tables and adding data to the tables
cur.execute('CREATE TABLE IF NOT EXISTS drivers (first_name, last_name, uuid)')
conn.commit()

cur.execute('CREATE TABLE IF NOT EXISTS hotels (name, address, uuid)')
conn.commit()

cur.execute('CREATE TABLE IF NOT EXISTS trips (driver_id, hotel_id, start_time, delivery_time, rating)')
conn.commit()

# Insert data
drivers.to_sql("drivers", conn, if_exists='replace', index=False)
drivers.to_sql("hotels", conn, if_exists='replace', index=False)
drivers.to_sql("trips", conn, if_exists='replace', index=False)