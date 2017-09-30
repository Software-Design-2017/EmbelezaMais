from django.core.exceptions import ValidationError


def validate_name(name):
    if len(name) > 120:
        raise ValidationError('Nome inválido maior que 120 caracteres.')
    if len(name) < 4:
        raise ValidationError('Nome inválido menor que 4 caracteres.')


def validate_description(description):
    if len(description) > 500:
        raise ValidationError(('Descrição inválida maior que 500 caracteres.'))


def validate_part(part):
    if part > 3:
        raise ValidationError('Selecione uma opção.')
    if part < 1:
        raise ValidationError('Selecione uma opção.')


def validate_price(price):
    if price <= 0:
        raise ValidationError('Preço inválido.')


def validate_face_part(face_part):
    if (face_part) > 5:
        raise ValidationError('Selecione uma opção.')
    if (face_part) < 1:
        raise ValidationError('Selecione uma opção.')


def validate_specific_hair(specific_hair):
    if (specific_hair) > 4:
        raise ValidationError('Selecione uma opção.')
    if (specific_hair) < 1:
        raise ValidationError('Selecione uma opção.')


def validate_style(style):
    if len(style) > 120:
        raise ValidationError('Estilo inválido maior que 120 caracteres.')
    if len(style) < 4:
        raise ValidationError('Estilo inválido menor que 4 caracteres.')
