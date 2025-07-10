import pandas as pd
from sqlalchemy import create_engine
import os

url=os.getenv("POSTGRESQL")

connection=create_engine(url)

data = pd.read_csv("./data/clients.csv")

def add_data_to_BD(data):
  data.to_sql("clients", con=connection, if_exists="replace", index=True )

add_data_to_BD(data)

clients = pd.read_sql("SELECT name, email, country FROM clients WHERE country LIKE 'Colombia'", con=connection)

clients.to_csv("./data/clientes_colombia.csv")
