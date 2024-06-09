import os
from dotenv import load_dotenv

import requests
from pprint import pprint

import pandas as pd

import psycopg2
from psycopg2 import sql



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
        # Load data
        df = pd.read_csv('sample_hpdata.csv')

        # Ensure data types are correct
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['Bedrooms'] = pd.to_numeric(df['Bedrooms'], errors='coerce')
        df['Bathrooms'] = pd.to_numeric(df['Bathrooms'], errors='coerce')
        df['SqFt'] = pd.to_numeric(df['SqFt'], errors='coerce')
        df['YearBuilt'] = pd.to_numeric(df['YearBuilt'], errors='coerce')
        df['LastSoldDate'] = pd.to_datetime(df['LastSoldDate'], errors='coerce')

        create_table = """
            CREATE TABLE IF NOT EXISTS ukprices (
              id SERIAL PRIMARY KEY,
              price INT,
              bedrooms INT,
              bathrooms INT,
              sqft INT,
              location VARCHAR,
              yearbuilt INT,
              lastsolddate DATE  
            );
        """
        cur.execute(create_table)

        insert_script = """
            INSERT INTO ukprices (price, bedrooms, bathrooms, sqft, location, yearbuilt, lastsolddate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """