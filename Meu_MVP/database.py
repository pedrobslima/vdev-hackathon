from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Substitua pelos seus dados reais
DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/avaliacao"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()