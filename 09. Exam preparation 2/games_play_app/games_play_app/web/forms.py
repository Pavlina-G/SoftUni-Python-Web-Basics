from django import forms

from games_play_app.web.models import Profile, Game


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(
                attrs={
                    'autocomplete': 'on',
                    'class': "form-control",
                    'toggle-password'
                    'onclick': "togglePassword()",
                }
            )
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance

    def _set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            "password": forms.PasswordInput(
                attrs={'placeholder': '********', 'autocomplete': 'on', 'class': 'form-control'}),
        }
        labels = {
            'image': 'Image URL',
        }


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
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
