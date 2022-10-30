from django import forms

from online_library.library_web.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_disabled_fields()

    def _set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # labels = {
        #     'title': 'Title'
        # }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),
        }


class CreateBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass

# class DeleteBookForm(BaseBookForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._set_disabled_fields()
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
#
#     def _set_disabled_fields(self):
#         for _, field in self.fields.items():
#             field.widget.attrs['readonly'] = 'readonly'
