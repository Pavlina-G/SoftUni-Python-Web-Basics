from datetime import date


def validate_before_today(value):
    # if invalid - raise ValidationError
    if date.today() < value:
        raise ValueError(f'{value} is not valid')