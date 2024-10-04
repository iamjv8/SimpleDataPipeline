import pandas as pd
from sqlalchemy import create_engine

# Created Engine for Postgres
engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5431/postgres')

# Read data from CSV file
coffee = pd.read_csv('./data/coffee.csv')

# Doing some transformation
# Added new column for revenue using existing column data
coffee['Revenue'] = coffee['Units Sold'] * coffee['Price']

# Writing data in Postgres table
coffee.to_sql(name='Coffee_Sell', con=engine, if_exists='replace')

