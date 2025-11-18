# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from spam_model import predecir_mensaje

app = FastAPI(
    title="Servicio de detección de SPAM",
    version="1.0.0"
)

class MensajeEntrada(BaseModel):
    mensaje: str

class RespuestaSpam(BaseModel):
    mensaje: str
    es_spam: bool
    etiqueta: int  # 0 = no spam, 1 = spam

@app.get("/")
def root():
    return {"status": "ok", "message": "Servicio de SPAM funcionando"}

@app.post("/predict", response_model=RespuestaSpam)
def predict(mensaje_entrada: MensajeEntrada):
    etiqueta = predecir_mensaje(mensaje_entrada.mensaje)
    es_spam = etiqueta == 1
    return RespuestaSpam(
        mensaje=mensaje_entrada.mensaje,
        es_spam=es_spam,
        etiqueta=etiqueta
    )
