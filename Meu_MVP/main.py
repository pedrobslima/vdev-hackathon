from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- AVALIAÇÕES SIMPLES ---
@app.post("/avaliacoes/")
def criar_avaliacao(avaliacao: schemas.AvaliacaoCreate, db: Session = Depends(get_db)):
    db_avaliacao = models.Avaliacao(**avaliacao.dict())
    db.add(db_avaliacao)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

@app.get("/avaliacoes/{colaborador_id}")
def listar_avaliacoes(colaborador_id: int, db: Session = Depends(get_db)):
    return db.query(models.Avaliacao).filter(models.Avaliacao.colaborador_id == colaborador_id).all()

@app.put("/avaliacoes/{avaliacao_id}")
def atualizar_avaliacao(avaliacao_id: int, dados: schemas.AvaliacaoUpdate, db: Session = Depends(get_db)):
    avaliacao = db.query(models.Avaliacao).filter(models.Avaliacao.id == avaliacao_id).first()
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    avaliacao.nota = dados.nota
    avaliacao.justificativa = dados.justificativa
    db.commit()
    return avaliacao

# --- AUTOAVALIAÇÃO COMPLETA ---
@app.post("/skills/")
def criar_skill(dados: schemas.SkillCreate, db: Session = Depends(get_db)):
    nova = models.Skill(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"status": "sucesso", "id": nova.id}


    #@app.get("/socios/colaboradores")
#def listar_colaboradores_autoavaliacoes(db: Session = Depends(get_db)):
    nomes = db.query(models.AutoAvaliacao.nome_usuario).distinct().all()
    return [nome[0] for nome in nomes]

    #@app.get("/socios/evolucao/{nome_usuario}")
#def evolucao_autoavaliacao(nome_usuario: str, db: Session = Depends(get_db)):
    avaliacoes = db.query(models.AutoAvaliacao).filter(models.AutoAvaliacao.nome_usuario == nome_usuario).all()

    if not avaliacoes:
        raise HTTPException(status_code=404, detail="Colaborador não encontrado ou sem autoavaliações.")

    resultados = []
    for a in avaliacoes:
        criterios = [
            a.sentimento_dono, a.resiliencia, a.organizacao, a.aprendizado,
            a.team_player, a.qualidade, a.prazos, a.eficiencia, a.criatividade
        ]
        media = round(sum(criterios) / len(criterios), 2)

        classificacao = (
            "Excepcional" if media > 4 else
            "Muito bom" if media >= 3.5 else
            "Fez o básico" if media >= 3 else
            "Precisa melhorar"
        )

        resultados.append({
            "id": a.id,
            "media": media,
            "classificacao": classificacao
        })

    return {
        "colaborador": nome_usuario,
        "avaliacoes": resultados
    }

