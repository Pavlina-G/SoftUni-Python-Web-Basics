from django.shortcuts import render, redirect

from car_collection_app.car_collection.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from car_collection_app.car_collection.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def catalogue(request):
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    if profile.full_name:
        name = profile.full_name
    elif profile.first_name and not profile.last_name:
        name = profile.first_name
    else:
        name = profile.last_name

    total_car_price = sum([x.price for x in Car.objects.all()])

    context = {
        'profile': profile,
        'name': name,
        'total_car_price': total_car_price,
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'cars/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'cars/car-delete.html', context)
