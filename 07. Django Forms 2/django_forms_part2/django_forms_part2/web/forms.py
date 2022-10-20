import uuid

from django import forms
from django.core.exceptions import ValidationError

from django_forms_part2.web.model_validators import validate_max_todos_per_person
from django_forms_part2.web.models import Todo, Person
from django_forms_part2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
        error_messages={
            'required': 'Todo text must be set'
        }
    )
    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
            # validate_priority,
            # MinValueValidator(1),
            # validators.MaxValueValidator(10),

        ),
    )

    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     raise ValidationError('Error 11')
    #
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        '''
        Used for:
        1. Transform data into desired format/form
        2. Validation
        :return:
        '''
        return self.cleaned_data['text'].lower()

    # 2. Validation
    # def clean_assignee(self):
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     # print(self.cleaned_data['assignee']) # keeps Person obj.
    #     return assignee

    # 1. Transform data into desired format/form
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']

        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')

        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = str(uuid.uuid4())
        return profile_image

    # def clean(self):
    #     super().clean()  # After this, all values are in `cleaned_data`
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']
    #

