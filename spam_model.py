# spam_model.py
import re
import joblib
from scipy.sparse import hstack

# Cargar modelo y vectorizador desde disco
mejor_modelo = joblib.load('mejor_modelo.pkl')
vectorizador = joblib.load('vectorizador.pkl')

def limpiar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
    return texto

def predecir_mensaje(texto: str) -> int:
    """
    Devuelve:
      0 -> NO SPAM
      1 -> SPAM
    """
    texto_limpio = limpiar_texto(texto)

    # transformar texto
    X_texto_nuevo = vectorizador.transform([texto_limpio])

    # longitud del mensaje
    long_nueva = len(texto_limpio.split())
    X_long_nuevo = [[long_nueva]]

    # combinar atributos texto + longitud
    X_nuevo = hstack([X_texto_nuevo, X_long_nuevo])

    etiqueta_pred = mejor_modelo.predict(X_nuevo)[0]
    return int(etiqueta_pred)
