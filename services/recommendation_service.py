from infrastructure import gemini_client, validator, parser, prompt_builder
from domain import exceptions, input_validator
from config import secrets


def recommend(area, level):

    area = input_validator.input_validation(area)

    if area is None:
        raise exceptions.ValueNotFound

    api_key, model = secrets.get_secrets()

    prompt = prompt_builder.make_prompt(area, level)

    response = gemini_client.search_courses(prompt, api_key, model)

    unvalidated_courses = parser.parse_cursos(response)

    return validator.validate_courses(unvalidated_courses)