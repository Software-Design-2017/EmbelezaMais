# Project name.
PROJECT_NAME = 'EmbelezaMais'

# EMAIL FIELDS.
EMAIL_FIELD_LENGTH = 30

# NAME FIELDS.
NAME_FIELD_LENGTH = 60

# NAME VALIDATION MESSAGES
NAME_SIZE = 'Your name exceeds 60 characteres'
NAME_CHARACTERS = 'Your name can\'t have special characters'

# EMAIL VALIDATION MESSAGES.
EMAIL_FORMAT = 'Enter a valid email address'

# ACCOUNT VERIFICATION EMAIL INFO.
EMAIL_CONFIRMATION_SUBJECT = 'Confirmação da Conta'
EMAIL_CONFIRMATION_BODY = """
                          Ola, obrigado por se registrar.
                          Para ativar sua conta clique nesse link em menos de
                          48 horas: http://127.0.0.1:8000/user/confirm/%s

                           """

EMBELEZAMAIS_EMAIL = 'embelezamais@gmail.com'

# PASSWORD FIELDS
PASSWORD = 'Password'
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 12

# PASSWORD VALIDATION MESSAGES.
PASSWORD_SIZE = 'Password must be between 8 and 12 characters'

# ERROR LOGIN
MESSAGE_LOGIN_COMPANY_ERROR = 'You are not registered as a company.'
MESSAGE_LOGIN_ERROR = 'Password and/or Email invalid.'

GENRE_CHOICES = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Unissex', 'Unissex'))
