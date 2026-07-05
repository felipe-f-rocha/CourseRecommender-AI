from google.genai.errors import APIError
from domain.exceptions import ValueNotFound, InvalidInput, ConfigurationError

def get_message(error):

    if isinstance(error, ValueNotFound):
        return 'O campo de área não pode estar vazio.'

    if isinstance(error, InvalidInput):
        return 'Input invalido. Tente novamente!!'

    if isinstance(error, APIError):
        match error.code:
            case 503:
                return 'O serviço pode estar temporariamente sobrecarregado.'
            case 403:
                return 'Verifique se a chave de API está definida e tem o acesso correto.'
            case 500:
                return 'Ocorre um erro inesperado. Tente novamente mais tarde'
            case 429:
                return 'Nosso serviço está indisponivel no momento, Tente novamente mais tarde!!'
            case _:
                return 'Houve um erro desconhecido. Tente novamente mais tarde!!'

    if isinstance(error, ConfigurationError):
        return 'Falha em acessar as credenciais de modelo.'

    else:
        return 'Ocorreu um erro!!'