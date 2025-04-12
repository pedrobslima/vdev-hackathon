from sqlalchemy import Column, Integer, String, Float, Text, Date
from database import Base

class AutoAvaliacao(Base):
    __tablename__ = "autoavaliacoes"
    id = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String(255))
    sentimento_dono = Column(Integer)
    resiliencia = Column(Integer)
    organizacao = Column(Integer)
    aprendizado = Column(Integer)
    team_player = Column(Integer)
    qualidade = Column(Integer)
    prazos = Column(Integer)
    eficiencia = Column(Integer)
    criatividade = Column(Integer)
    media = Column(Float)


