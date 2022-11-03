from django.core.exceptions import ValidationError


def validate_min_len_username(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_years(value):
    min_year = 1980
    max_year = 2049
    if value < min_year or value > max_year:
        raise ValidationError('Year must be between 1980 and 2049')
