from sqlalchemy import create_engine
import pandas as pd
import subprocess

proc = subprocess.Popen('heroku config:get DATABASE_URL -a adrestia', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
db_url = db_url[:8]+'+psycopg2'+db_url[8:]
print(db_url)
engine = create_engine(db_url)
df = pd.read_csv('data/APPM.csv')
df.to_sql(con=engine, name='appm', if_exists='replace', index=True)


