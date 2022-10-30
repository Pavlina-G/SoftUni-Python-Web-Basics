from django.shortcuts import render, redirect

from online_library.library_web.forms import CreateProfileForm, CreateBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from online_library.library_web.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return add_profile(request)

    context = {
        'books': Book.objects.all(),
        'profile': profile,
    }

    return render(request, 'home/home-with-profile.html', context)


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        # 'hide_nav_links': True,
    }

    return render(request, 'home/home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
        'profile': profile,
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
        'profile': profile
    }

    return render(request, 'profiles/delete-profile.html', context)


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    profile = get_profile()

    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'books/book-details.html', context)


def add_book(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateBookForm()
    else:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,

    }

    return render(request, 'books/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    profile = get_profile()

    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'book': book,
        'form': form,
        'profile': profile,
    }
    return render(request, 'books/edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')



