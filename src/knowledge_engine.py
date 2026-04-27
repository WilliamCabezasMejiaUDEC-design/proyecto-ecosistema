import json
import os

def get_hardcoded_knowledge():
    """Respaldo crítico: Si el JSON falla, el bot mantiene su identidad base."""
    return {
        "identidad": "El proyecto 4R+T es un ecosistema de inteligencia circular en el Sumapaz.",
        "mega_2028": "Transformar 10.000 toneladas de residuos en un fondo para 5.000 becas educativas.",
        "estetica": "Electric Gold: Dorado sobre Negro."
    }

def cargar_conocimiento():
    """
    Lee el archivo JSON desde /data/knowledge.json.
    Utiliza una ruta relativa dinámica para funcionar en cualquier entorno.
    """
    # sube un nivel desde 'src/' a la raíz del proyecto, luego entra a 'data/'
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        # Si falla (archivo no existe o JSON corrupto), usa el respaldo
        return get_hardcoded_knowledge()

def construir_prompt_maestro(pregunta):
    """Construye el contexto para evitar alucinaciones."""
    data = cargar_conocimiento()
    contexto = json.dumps(data, ensure_ascii=False)
    
    return f"""
    Eres el consultor experto del Ecosistema 4R+T. 
    Tu objetivo es responder consultas basándote estrictamente en el siguiente contexto:
    {contexto}
    
    Instrucciones:
    1. Responde de forma profesional, concisa y técnica.
    2. Si la respuesta no está en el contexto, indica que es un tema en desarrollo.
    
    Pregunta del usuario: {pregunta}
    """