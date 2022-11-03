from django.core import validators
from django.db import models

from car_collection_app.car_collection.validators import validate_min_len_username, validate_years


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 10
    MIN_AGE = 18
    MAX_LEN_PASSWORD = 30
    MAX_LEN_NAMES = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validate_min_len_username,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAMES,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAMES,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2
    MIN_PRICE = 1

    SPORT_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = (
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MODEL),
        ),
        null=False,
        blank=False,
    )

    year = models.PositiveIntegerField(
        validators=(
            validate_years,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)
