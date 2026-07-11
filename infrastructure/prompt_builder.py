def make_prompt(area:str, escolaridade:str, level:str) -> str:
    # Formação do Prompt base da IA

    prompt = (f'''Busque cursos para mim seguindo as seguintes informações:

            área = {area},
            minha escolaridade - {escolaridade},
            nivel do curso desejado = {level}

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

    return prompt