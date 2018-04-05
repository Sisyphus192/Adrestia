from sqlalchemy import create_engine
import pandas as pd
import subprocess
import psycopg2
import os

proc = subprocess.Popen('heroku config:get DATABASE_URL -a adrestia', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
db_url = db_url[:8]+'ql'+db_url[8:]
#DATABASE_URL = os.environ['DATABASE_URL']
#print(DATABASE_URL)
#print(db_url)
#conn = psycopg2.connect(db_url)
engine = create_engine(db_url)
df = pd.read_csv('data/APPM.csv')
print('hello')
df[:10].to_sql(con=engine, name='courses', if_exists='replace', index=True)
print('hello2')
