from google import genai
from google.genai import types

def search_courses(prompt, api_key, model):
    # Definição de modelo e instrução do modelo
    print(api_key)

    client = genai.Client(api_key=api_key)

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch())

    courses = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="""
                    Você é um especialista em educação.

                    REGRAS CRÍTICAS:
                    - Nunca invente cursos
                    - Nunca invente links
                    - Se não tiver certeza, não responda
                    - Sempre forneça link direto válido
                    - Respostas curtas e organizadas
                    """,
            tools=[grounding_tool],
            temperature=0.3,
        )
    )

    return courses