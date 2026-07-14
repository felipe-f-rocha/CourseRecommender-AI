def parse_cursos(courses) -> list[dict[str, str]]:
    # Remove caracteres desnecesários e quebra o retorno em linhas

    courses = courses.text.replace('*', '').replace('{', '').replace('}', '')
    formatted_courses = courses.split('\n')

    formatted_courses = [
        item for item in formatted_courses
        if item.strip()
    ]

    actual_course = {}
    final_courses = []

    # Separa os textos tratados em dicionarios por cursos

    for i in formatted_courses:

        linha = i.lower()
        if "nome do curso" in linha:
            if actual_course:
                final_courses.append(actual_course)

            actual_course = {
                "Nome do Curso": i.split(":", 1)[1].strip().title() if ":" in i else ""
            }

        elif 'plataforma' in linha:
            actual_course["Plataforma"] = i.split(":", 1)[1].strip().title()
        elif 'link' in linha:
            actual_course["Link"] = i.split(":", 1)[1].strip()
        elif 'por que é ideal' in linha:
            actual_course["Por que é ideal"] = i.split(":", 1)[1].strip().capitalize()
        elif 'é gratuito:' in linha:
            actual_course["É gratuito"] = i.split(":", 1)[1].strip().capitalize()

    if actual_course:
        final_courses.append(actual_course)

    return final_courses