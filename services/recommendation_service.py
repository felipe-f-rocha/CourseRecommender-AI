from infrastructure import gemini_client, validator
from domain import prompt_builder, parser
from config import secrets

def recommend(area, level):

    api_key, model = secrets.get_secrets()

    prompt = prompt_builder.make_prompt(area, level)

    response = gemini_client.search_courses(prompt, api_key, model)

    unvalidated_courses = parser.parse_cursos(response)

    return validator.validate_courses(unvalidated_courses)