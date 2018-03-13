import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://root:@localhost:3306/adrestiaDB")

df = pd.read_csv('data/APPM.csv')
df.to_sql(con=engine, name='courses', if_exists='replace', index=False)


