from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from exam_prep.music_app.validators import validate_only_alphanumeric

'''
•	Profile
    o	Username
        	Character field, required.
        	It should have at least 2 characters and maximum - 15 characters.
        	The username can consist only of letters, numbers, and underscore ("_"). 
        Otherwise, raise a ValidationError with the message: 
        "Ensure this value contains only letters, numbers, and underscore."
    o	Email
        	Email field, required.
    o	Age
        	Integer field, optional.
        	The age cannot be below 0.
'''


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validate_only_alphanumeric,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


'''
•	Album
    o	Album Name
        	Character field, required.
        	All album names must be unique.
        	 It should consist of a maximum of 30 characters.
    o	Artist
        	Character field, required.
        	It should consist of a maximum of 30 characters.
    o	Genre
        	Char field, required.
        	It should consist of a maximum of 30 characters.
        	The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
    o	Description
        	Text field, optional.
    o	Image URL
        	URL field, required.
    o	Price
        	Float field, required.
        	The number of decimal places of the price should not be specified in the database.
        	The price cannot be below 0.0.
'''


# With enums
class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'Artist `{self.artist}`, Album `{self.album_name}`'
# Without enums
# class Album(models.Model):
#     MAX_LEN_NAME = 30
#     MAX_LEN_ARTIST = 30
#     MAX_LEN_GENRE = 30
#
#     POP_MUSIC = "Pop Music"
#     JAZZ_MUSIC = "Jazz Music"
#     RNB_MUSIC = "R&B Music"
#     ROCK_MUSIC = "Rock Music"
#     COUNTRY_MUSIC = "Country Music"
#     DANCE_MUSIC = "Dance Music"
#     HIP_HOP_MUSIC = "Hip Hop Music"
#     OTHER_MUSIC = "Other"
#
#     MUSICS = (
#         (POP_MUSIC, POP_MUSIC),
#         (JAZZ_MUSIC, JAZZ_MUSIC),
#         (RNB_MUSIC, RNB_MUSIC),
#         (ROCK_MUSIC, ROCK_MUSIC),
#         (COUNTRY_MUSIC, COUNTRY_MUSIC),
#         (DANCE_MUSIC, DANCE_MUSIC),
#         (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
#         (OTHER_MUSIC, OTHER_MUSIC),
#     )
#
#     album_name = models.CharField(
#         max_length=MAX_LEN_NAME,
#         unique=True,
#         null=False,
#         blank=False,
#     )
#
#     artist = models.CharField(
#         max_length=MAX_LEN_ARTIST,
#         null=False,
#         blank=False,
#     )
#
#     genre = models.CharField(
#         max_length=MAX_LEN_GENRE,
#         choices=MUSICS,
#         null=False,
#         blank=False,
#     )
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     image_url = models.URLField(
#         null=False,
#         blank=False,
#     )
#
#     price = models.FloatField(
#         null=False,
#         blank=False,
#         validators=(
#             validators.MinValueValidator(0.0),
#         )
#     )
#
#     class Meta:
#         ordering = ('pk',)
#
#     def __str__(self):
#         return f'Artist `{self.artist}`, Album `{self.album_name}`'
