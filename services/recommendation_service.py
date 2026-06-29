from infrastructure import gemini_client, validator, parser, prompt_builder
from domain import exceptions, input_validator
from config import secrets
from google.genai import errors
from time import sleep


def recommend(area, level):

    area = input_validator.input_validation(area)

    if area is None:
        raise exceptions.ValueNotFound

    api_key, model, fallback_model = secrets.get_secrets()

    prompt = prompt_builder.make_prompt(area, level)

    response = None

    try:
        response = gemini_client.search_courses(prompt, api_key, model)
    except errors.APIError as e:
        if e.code == 429:
            sleep(2)
            response = gemini_client.search_courses(prompt,api_key,fallback_model)

    unvalidated_courses = parser.parse_cursos(response)

    return validator.validate_courses(unvalidated_courses)