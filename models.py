import os
from dotenv import load_dotenv

import psycopg2

load_dotenv('.env')

conn_params = {
    'host': os.getenv('H_NAME'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('UNAME'),
    'password': os.getenv('PASSWORD'),
    'port': os.getenv('PORT')
}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS ukprices(id SERIAL PRIMARY KEY, price INT, bedrooms INT, bathrooms INT, sqft INT, Location VARCHAR, yearbuilt INT, lastsolddate DATE);")
