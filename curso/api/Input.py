import datetime

def to_int(value):
    try:
        return int(value)
    except:
        return 0

def to_float(value):
    try:
        return float(value)
    except:
        return 0.0

def to_complex(value):
    try:
        return complex(value)
    except:
        return 0j

def to_bool(value):
    try:
        return bool(value)
    except:
        return False

def to_datetime(value):
    pass
