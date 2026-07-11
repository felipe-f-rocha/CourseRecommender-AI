from domain.exceptions import InvalidInput


def is_empty(area:str) -> str:
    # Checks if the input is an empty string

    if not area or not area.strip():
        raise InvalidInput('Nome de área não pode estar vazio.')
    return area

def check_length(area:str) -> str:

    if len(area) < 2:
        raise InvalidInput('Nome de área incompleto')
    elif len(area) > 80:
        raise InvalidInput('Tamanho de área excedeu limite de caracteres.')

    return area

def check_number(area:str) -> str:
    nums = 0
    for i in area:
        if i.isnumeric():
            nums+=1

    if len(area.replace(' ', '')) == nums:
        raise InvalidInput('Nome de área não pode conter somente números.')

    return area