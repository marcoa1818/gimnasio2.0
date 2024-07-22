from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://avnadmin:AVNS_RSH4dsc8x0wTx6SWfV4@mysql-10da6282-amelipg.e.aivencloud.com:22252/defaultdb'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3307/test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
