from domain.exceptions import InvalidInput
from domain import input_validations

def validate(area):

    try:
        area = input_validations.is_empty(area)
        area = input_validations.check_length(area)
        area = input_validations.check_number(area)
    except InvalidInput:
        raise 'Invalid Input'
    else:
        return area