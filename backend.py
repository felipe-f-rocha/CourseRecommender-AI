from concurrent.futures.thread import ThreadPoolExecutor

import google.genai.errors
from google import genai
import tomllib
from google.api_core.exceptions import ClientError
from google.genai import types
import requests
import streamlit as st


# Verify if the right file had been initiated

if __name__ == "__main__":
        raise ValueError('''O arquivo errado foi iniciado.
        Para rodar o programa digite no terminal 'streamlit run app.py' ''')

# Create User Agent for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36 CursoRecommender/1.0"
}

# Load the API key and AI Model from secrets

with open('secrets.toml', 'rb') as f:
    config = tomllib.load(f)

try:
    api_key = config ["GEMINI"]["GEMINI_API_KEY"]
    model = config["GEMINI"]["GEMINI_MODEL"]
except KeyError:
    api_key = st.secrets["GEMINI_API_KEY"]
    model = st.secrets["GEMINI_MODEL"]

if not api_key:
    raise ValueError("Erro: Chave de API não encontrada")

if not model:
    raise ValueError("Erro: Modelo não encontrado")

client = genai.Client(api_key=api_key)

# Adiciona mecanismo de pesquisa google ao modelo

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

def make_prompt(area, nivel):
    # Formação do Prompt base da IA

    prompt = (f'''Busque cursos para mim seguindo as seguintes informações:

            área = {area},
            meu nível = {nivel}

            Se não conseguir seguir, NÃO responda:

                {{
                1. Nome do curso:
                Plataforma:
                Link:
                Por que é ideal:
                É gratuito: 
            }}

            Regras:
            - Use APENAS cursos reais
            - Inclua LINK DIRETO
            - Não repita cursos
            - Máximo 5 cursos
            - Seja direto
            - Para cada curso, indique claramente se ele é gratuito e COMO acessar gratuitamente (ex: audit, free tier).
             Se não for possível, não inclua. Dê preferência para cursos com financial aid ou certificado gratis
            ''')

    return search_courses(prompt, model)

def search_courses(prompt, model):
    # Definição de modelo e instrução do modelo
        cursos = client.models.generate_content(
            model=model,
            contents= prompt,
            config= types.GenerateContentConfig(
                system_instruction="""
                    Você é um especialista em educação.
    
                    REGRAS CRÍTICAS:
                    - Nunca invente cursos
                    - Nunca invente links
                    - Se não tiver certeza, não responda
                    - Sempre forneça link direto válido
                    - Respostas curtas e organizadas
                    """,
                tools = [grounding_tool],
                temperature=0.3,
                )
            )

        return formatter(cursos)

def formatter(cursos):

    # Remove caracteres desnecesários e quebra o retorno em linhas

    cursos = cursos.text.replace('*','').replace('{','').replace('}','')
    cursos_formatados = cursos.split('\n')
    temporario = []

    # Remove linhas vazias

    for item in cursos_formatados:
        if item == '':
            continue
        else:
            temporario.append(item)

    cursos_formatados = temporario
    curso_atual = {}
    cursos_finais = []

    # Separa os textos tratados em dicionarios por cursos

    for i in cursos_formatados:

        i = i.lower()
        if "nome do curso" in i:
            if curso_atual:
                cursos_finais.append(curso_atual)

            curso_atual = {
                "Nome do Curso": i.split(":", 1)[1].strip().title() if ":" in i else ""
            }

        elif 'plataforma' in i:
            curso_atual["Plataforma"] = i.split(":", 1)[1].strip().title()
        elif 'link' in i:
            curso_atual["Link"] = i.split(":", 1)[1].strip()
        elif 'por que é ideal' in i:
            curso_atual["Por que é ideal"] = i.split(":", 1)[1].strip().capitalize()
        elif 'é gratuito:' in i:
            curso_atual["É gratuito"] = i.split(":", 1)[1].strip().capitalize()

    if curso_atual:
        cursos_finais.append(curso_atual)

    # Trabalha simultaneamente em multiplas requests de validação

    with ThreadPoolExecutor(max_workers = 5) as pool:
        cursos_finais = list(pool.map(url_validation, cursos_finais))

    return cursos_finais


def url_validation(curso):
    # Valida as URLs e as substitui caso não sejam encontradas

    try:
        r = requests.head(curso["Link"], headers=headers,timeout=2  )
        # Verifica a URL é funcional
        if r.status_code < 400:
            pass
        else:
            r = requests.get(curso["Link"], headers=headers, timeout=5)
            if r.status_code < 400:
                pass
            else:
                busca = curso['Nome do Curso'].replace(' ', '+')
                curso["Link"] = 'https://www.google.com/search?q=' + busca

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException):
            busca = curso['Nome do Curso'].replace(' ', '+')
            curso["Link"] = 'https://www.google.com/search?q=' + busca

    return curso