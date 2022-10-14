from django import forms
from django.shortcuts import render

from django_forms.forms_demos.forms import PersonForm
from django_forms.forms_demos.models import Person, Pet


def index_form(request):
    name = None
    # form = NameForm(request.POST or None)
    if request.method == 'GET':
        form = PersonForm()
    else:  # request.method == 'post'
        form = PersonForm(request.POST)
        if form.is_valid():  # is_valid() - validates the form, returns True or False and fills cleaned_data - {}
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name
            )

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    # )
    class Meta:
        model = Person
        fields = '__all__'  # or
        # fields = ('name', 'age') # include
        # exclude = ('pets',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
        help_texts = {
            'name': 'Your name',
        }
        labels = {
            'age': 'Your age'
        }


def index_model_form(request):
    # instance = Person.objects.get(pk=2)
    if request.method == 'GET':
        form = PersonCreateForm  # (instance=instance)
    else:
        form = PersonCreateForm(request.POST)  # ( instance=instance)
        if form.is_valid():
            form.save()  # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html', context)


def related_models_demo(request):
    pet = Pet.objects.get(pk=1)
    person = Person.objects.get(pk=1)
    # pet.person
    # person.pets # Person has `pets` field
    # pet.person_set # Pet has no `person` field