from django.core.exceptions import ValidationError

def validate_name(name):
    if len(name) > 120:
        raise ValidationError('Nome inválido!Maior que 120 caracteres.')
    if len(name) < 4:
        raise ValidationError('Nome inválido menor que 4 caracteres.')


def validate_price(price):
    if(price < 0):
        raise ValidationError('Preço não pode ter um valor negativo!')
