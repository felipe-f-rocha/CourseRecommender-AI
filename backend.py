import os
from concurrent.futures.thread import ThreadPoolExecutor
from google import genai
from dotenv import load_dotenv
from google.genai import types
import requests
import streamlit as st

# Verifica se o arquivo correto foi iniciado

if __name__ == "__main__":
        raise ValueError('''O arquivo errado foi iniciado.
        Para rodar o programa digite o terminal 'streamlit run app.py' ''')

# Cria User-Agent para requests de validação
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36 CursoRecommender/1.0"
}

# Traz a API_KEY de .env e a carrega

load_dotenv()

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    model = st.secrets["GEMINI_MODEL"]
except:
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL")

if not api_key:
    raise ValueError("Erro: Chave de API não encontrada")

if not model:
    raise ValueError("Erro: Modelo não encontrado")

client = genai.Client(api_key=api_key)

# Adiciona mecanismo de pesquisa google ao modelo

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

def formar_prompt(area, nivel):
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
             Se não for possível, não inclua.
            ''')

    return buscar_cursos(prompt)


def buscar_cursos(prompt):
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
    return formatar(cursos)



def formatar(cursos):

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
        cursos_finais = list(pool.map(validacao_de_url, cursos_finais))

    return cursos_finais


def validacao_de_url(curso):
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