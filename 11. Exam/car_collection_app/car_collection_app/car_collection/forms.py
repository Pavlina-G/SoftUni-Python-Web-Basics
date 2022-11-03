from django import forms
from django.core import validators

from car_collection_app.car_collection.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = '__all__'
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class DeleteProfileForm(BaseProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def _set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image_URL',
            'price': 'Price',
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def _set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
