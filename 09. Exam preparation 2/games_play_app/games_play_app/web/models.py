from django.core import validators
from django.db import models

'''
•	Profile Model
    o	Email
        	Email field, required.
    o	Age
        	Integer field, required.
        	The age cannot be below 12.
    o	Password
        	Character (password) field, required.
        	It should consist of a maximum of 30 characters.
    o	First Name
        	Character field, optional.
        	It should consist of a maximum of 30 characters.
    o	Last Name
        	Character field, optional.
        	It should consist of a maximum of 30 characters.
    o	Profile Picture
        	URL field, optional.

'''


class Profile(models.Model):
    MIN_AGE = 12
    MAX_LEN_PASSWORD = 30
    MAX_LEN_NAME = 30

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
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.email

'''
•	Game Model
    o	Title
        	Character field, required.
        	It should consist of a maximum of 30 characters.
        	All game titles must be unique.
    o	Category
        	Character (choice) field, required.
        	It should consist of a maximum of 15 characters.
        	The choices are "Action", "Adventure", "Puzzle", "Strategy", "Sports", "Board/Card Game", and "Other".
    o	Rating
        	Float field, required.
        	The rating can be between 0.1 and 5.0 (both inclusive).
    o	Max Level
        	Integer field, optional.
        	The max level cannot be below 1.
    o	Image URL
        	URL field, required.
    o	Summary
        	Text field, optional.

'''


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    MIN_RATING = 0.1
    MAX_RATING = 0.5
    MIN_VALUE_LEVEL = 1

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    CATEGORIES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_RATING),
            validators.MaxValueValidator(MAX_RATING),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_VALUE_LEVEL),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.title
