import pandas as pd
from sqlalchemy import create_engine



engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5431/postgres')


coffee = pd.read_csv('./data/coffee.csv')

coffee['Revenue'] = coffee['Units Sold'] * coffee['Price']

coffee.to_sql(name='Coffee_Sell', con=engine, if_exists='replace')

