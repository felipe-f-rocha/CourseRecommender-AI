from google import genai
from google.genai import types

class GeminiClient:

    def __init__(self, api_key: str, model: str):
        self.model = model
        self.client = genai.Client(api_key=api_key)

        self.grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )

    def search_courses(self, prompt: str):
        return self.client.models.generate_content(
            model=self.model,
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
                tools=[self.grounding_tool],
                temperature=0.3,
            ),
        )