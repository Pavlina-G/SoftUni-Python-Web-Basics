from django.db import models


class Profile(models.Model):
    MAX_LEN_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_TYPE = 30

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'Book title: {self.title}'
