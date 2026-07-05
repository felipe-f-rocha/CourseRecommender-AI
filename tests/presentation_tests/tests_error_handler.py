import pytest
from domain.exceptions import ValueNotFound, InvalidInput, ConfigurationError
from presentation import error_handler
from google.genai.errors import APIError
class TestMyExceptions:

    @pytest.mark.parametrize(
        "insert, expected",
        [
            (ValueNotFound(), 'O campo de área não pode estar vazio.')
        ]
    )

    def test_ValueNotFound(self, insert,expected):
        result = error_handler.get_message(insert)

        assert result == expected

    @pytest.mark.parametrize(
        "insert, expected",
        [
            (InvalidInput(),'Input invalido. Tente novamente!!')
        ]
    )

    def test_InvalidInput(self,insert,expected):
        result = error_handler.get_message(insert)

        assert result == expected

    @pytest.mark.parametrize(
        "insert, expected",
        [
            (ConfigurationError, 'Falha em acessar as credenciais de modelo.')
        ]
    )

    def test_ConfigurationError(self,insert,expected):
        result = error_handler.get_message(insert)

        assert result == expected

class TestApiError:

    @pytest.mark.parametrize(
        "insert, expected",
        [   (APIError(code=403, response_json=True),
            'Verifique se a chave de API está definida e tem o acesso correto.'),

            (APIError(code=429, response_json=True),
             'Nosso serviço está indisponivel no momento, Tente novamente mais tarde!!'),

            (APIError(code=500, response_json=True),
             'Ocorre um erro inesperado. Tente novamente mais tarde'),

            (APIError(code=503, response_json=True),
             'O serviço pode estar temporariamente sobrecarregado.'),
        ]
    )

    def test_APIError(self,insert,expected):
        result = error_handler.get_message(insert)

        assert result == expected