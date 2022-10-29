from django.core import validators
from django.shortcuts import render, redirect
from django.db.models import Avg
from games_play_app.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from games_play_app.web.models import Profile, Game

'''
3.	Routes
•	http://localhost:8000/ - home page
•	http://localhost:8000/profile/create - create profile page
•	http://localhost:8000/dashboard/ - dashboard page
•	http://localhost:8000/game/create/ - create game page
•	http://localhost:8000/game/details/<id>/ - details game page
•	http://localhost:8000/game/edit/<id>/ - edit game page
•	http://localhost:8000/game/delete/<id>/ - delete game page
•	http://localhost:8000/profile/details/ - details profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page
'''


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_game():
    try:
        return Game.objects.get()
    except Game.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'hide_nav_links': True,
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfileForm
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def dashboard(request):
    profile = get_profile()

    if profile is None:
        return redirect('index')
    else:
        games = Game.objects.all()

    context = {
        'games': games,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)


def create_game(request):

    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
    }

    return render(request, 'games/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }
    return render(request, 'games/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'games/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'games/delete-game.html', context)


def details_profile(request):
    profile = get_profile()
    games_count = Game.objects.count()
    avg_rating = Game.objects.aggregate(Avg('rating'))
    average_rating = avg_rating['rating__avg']
    print(average_rating)
    no_rating = "0.0"
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
        'no_rating': no_rating,
    }

    return render(request, 'profiles/details-profile.html', context)


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
    }
    return render(request, 'profiles/edit-profile.html', context)


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

    return render(request, 'profiles/delete-profile.html', context)
