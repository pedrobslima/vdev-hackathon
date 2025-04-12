from pydantic import BaseModel
from datetime import date

class AutoAvaliacaoBase(BaseModel):
    nome_usuario: str
    sentimento_dono: int
    resiliencia: int
    organizacao: int
    aprendizado: int
    team_player: int
    qualidade: int
    prazos: int
    eficiencia: int
    criatividade: int
    media: float

class SkillCreate(BaseModel):
    nome: str
    criterio: str
    tipo: str
    nota: int
    justificativa: str | None = None
    data: date

class AvaliacaoBase(BaseModel):
    colaborador_id: int
    criterio: str
    nota: int
    justificativa: str

class AvaliacaoCreate(AvaliacaoBase):
    pass

class AvaliacaoUpdate(BaseModel):
    nota: int
    justificativa: str
