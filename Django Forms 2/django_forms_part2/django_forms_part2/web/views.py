from django import forms
# from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.core import validators
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_forms_part2.web.forms import TodoForm, TodoCreateForm, PersonCreateForm
from django_forms_part2.web.models import Person
from django_forms_part2.web.validators import validate_text, ValueInRangeValidator

#
# def index(request):
#     if request.method == 'GET':
#         form = TodoCreateForm()
#     else:
#         form = TodoCreateForm(request.POST)
#
#     if form.is_valid():
#         form.save()
#         # model = form.instance
#         # model.full_clean()  # model.forms inherit validators from the model and can be upgraded
#         return HttpResponse('All is valid')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'index.html', context)


def index(request):
    form_class = TodoForm
    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)

    if form.is_valid():
        return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)