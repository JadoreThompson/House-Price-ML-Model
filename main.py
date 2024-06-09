import requests
from pprint import pprint

import pandas as pd

import psycopg2
from psycopg2 import sql
import models

df = pd.read_csv('sample_hpdata.csv')
prices = df['Price'].tolist()

# with psycopg2.connect(**models.conn_params) as conn:
#     with conn.cursor() as cur:
#         insert_script = sql.SQL("""
#             INSERT INTO ukprices (price, bedrooms, bathrooms, sqft, location, yearbuilt, lastsolddate)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#             ON CONFLICT DO NOTHING;
#         """)
#
#         for index,row in df.iterrows():
#             cur.execute(insert_script, (
#                 row['Price'],
#                 row['Bedrooms'],
#                 row['Bathrooms'],
#                 row['SqFt'],
#                 row['Location'],
#                 row['YearBuilt'],
#                 row['LastSoldDate']
#             ))

with psycopg2.connect(**models.conn_params) as conn:
    with conn.cursor() as cur:
        db_query = """
            SELECT * FROM ukprices;
        """
        cur.execute(db_query)
        rows = cur.fetchall()

        all_prices = []
        for row in rows:
            all_prices.append(row[1])
        price_series = pd.Series(all_prices)
        average_price = price_series.mean()
        print("Mean Price: ", average_price)

        db_query = """
            SELECT * FROM ukprices
            WHERE location IN('London', 'Bristol');
        """
        cur.execute(db_query)
        rows = cur.fetchall()
        all_prices = []
        for row in rows:
            all_prices.append(row[1])
        price_series = pd.Series(all_prices)
        avse_price = price_series.mean()
        print("Mean SE Price: ", avse_price)

        db_query = """
            SELECT * FROM ukprices
            WHERE location IN ('Manchester', 'Liverpool', 'Leeds', 'Newcastle', 'Sheffield');
        """
        cur.execute(db_query)
        rows = cur.fetchall()
        all_prices = []
        for row in rows:
            all_prices.append(row[1])
        price_series = pd.Series(all_prices)
        avne_price = price_series.mean()
        print("Mean NE Price: ", avne_price)

        db_query = """
            SELECT * FROM ukprices
            WHERE location='Birmingham';
        """
        cur.execute(db_query)
        rows = cur.fetchall()
        all_prices = []
        for row in rows:
            all_prices.append(row[1])
        price_series = pd.Series(all_prices)
        avmid_price = price_series.mean()
        print("Mean Midlands Price: ", avmid_price)

        db_query = """
            SELECT * FROM ukprices
            WHERE location IN ('Glasgow', 'Edinburgh');
        """
        cur.execute(db_query)
        rows = cur.fetchall()
        all_prices = []
        for row in rows:
            all_prices.append(row[1])
        price_series = pd.Series(all_prices)
        avmid_price = price_series.mean()
        print("Mean Midlands Price: ", avmid_price)

        create_table = """
            CREATE TABLE IF NOT EXISTS averageprices(
                id SERIAL PRIMARY KEY,
                location varchar,
                avgprice INT
            );
        """
        cur.execute(create_table)

        insert_script = """
            INSERT INTO averageprices (location, avgprice)
            VALUES (%s, %s)
            ON CONFLICT (location) DO NOTHING;
        """
        insert_values = {
            'North England': avne_price,
            'South England': avse_price,
            'Midlands': avmid_price
        }

        for region, price in insert_values.items():
            cur.executemany(insert_script, (region, price))




