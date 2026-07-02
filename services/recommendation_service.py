from infrastructure import gemini_client, validator, parser, prompt_builder
from services import input_validator
from config import secrets
from google.genai import errors
from time import sleep


def recommend(area, level):

    area = input_validator.validate(area)

    api_key, model, fallback_model = secrets.get_secrets()

    prompt = prompt_builder.make_prompt(area, level)

    main_client = gemini_client.GeminiClient(api_key, model)
    fallback_client =gemini_client.GeminiClient(api_key, fallback_model)

    try:
        response = main_client.search_courses(prompt)
    except errors.APIError as e:
        if e.code == 429:
            sleep(2)
            response = fallback_client.search_courses(prompt)
        else:
            raise

    unvalidated_courses = parser.parse_cursos(response)

    return validator.validate_courses(unvalidated_courses)