from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import clickhouse_connect

Base = declarative_base()
DATABASE_URL = "postgresql://user:password@db:5432/app_db"
CLICKHOUSE_URL = "clickhouse://user:password@clickhouse:9000/app_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
clickhouse_client = clickhouse_connect.get_client(host='clickhouse', port=9000, user='user', password='password')
