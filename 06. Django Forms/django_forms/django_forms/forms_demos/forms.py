from django import forms


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )
    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name',
        widget=forms.TextInput(
            # This corresponds to HTML attributes
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }
        )
    )

    age = forms.IntegerField(
        required=False,
        help_text='Enter your age',
        # widget=forms.NumberInput(),  # default
        # initial=0
    )

    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput(),
    #     required=False,
    # )
    #
    # secret = forms.CharField(
    #     widget=forms.PasswordInput(),
    #     required=False,
    # )
    #
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    #     required=False,
    # )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select,  # Default
    )

    # occupancy2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect(),
    #     # widget=forms.SelectMultiple,
    # )
