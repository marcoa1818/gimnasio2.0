from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3307/test"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_mt_5rx22sKLMwKQUThg@mysql-169823ec-utxicotepec-mgr7.l.aivencloud.com:23905/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
