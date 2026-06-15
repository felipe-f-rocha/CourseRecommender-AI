from concurrent.futures import ThreadPoolExecutor
import requests
from functools import partial

def validate_courses(courses):
    # Create User Agent for requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36 CursoRecommender/1.0"
    }
    validator = partial(url_validation, headers)

    with ThreadPoolExecutor(max_workers=5) as pool:
        return list(pool.map(validator, courses))


def url_validation(headers,courses):
    # Valida as URLs e as substitui caso não sejam encontradas

    try:
        r = requests.head(courses["Link"], headers=headers,timeout=2  )
        # Verifica a URL é funcional
        if r.status_code < 400:
            pass
        else:
            r = requests.get(courses["Link"], headers=headers, timeout=5)
            if r.status_code < 400:
                pass
            else:
                busca = courses['Nome do Curso'].replace(' ', '+')
                courses["Link"] = 'https://www.google.com/search?q=' + busca

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException):
            
            busca = courses['Nome do Curso'].replace(' ', '+')
            courses["Link"] = 'https://www.google.com/search?q=' + busca

    return courses
