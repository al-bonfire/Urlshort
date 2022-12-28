from sqlalchemy import Column, String, Text, Integer, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config import settings as s
from time import sleep

LOGIN = f'{s.POSTGRES_USER}:{s.POSTGRES_PASSWORD}'

DATABASE_URI = f"postgresql+psycopg2://{LOGIN}@{s.POSTGRES_HOST}:{s.POSTGRES_PORT}/{s.POSTGRES_DB}"

Base = declarative_base()
engine = create_engine(DATABASE_URI)

loop = True
while loop:
    try:
        S = sessionmaker(engine)
        loop = False
        print('Conectado com sucesso!')
    except Exception as e:
        print(e)
        sleep(5)
    

class URL(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    url = Column(Text)
    token = Column(String(100))
    
def init_db():
    Base.metadata.create_all(engine)