class PersonalError(Exception):
    def __init__(self, message='El número no puede ser 13'):
        Exception.__init__(self, message)


class SubclassError(PersonalError):
    def __init__(self, message=''):
        PersonalError._init__(self, message)

a =  13
if a == 13:
    raise PersonalError
