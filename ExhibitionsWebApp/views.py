from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.


def main_page(request):
    return render(request, 'main_page.html', {})


# owner views
class OwnerView(ListView):
    model = Owner
    template_name = 'owner_page.html'
    queryset = Owner.objects.all()


class OwnerCreate(CreateView):
    model = Owner
    template_name = 'owner_form.html'
    form_class = OwnerForm
    success_url = '/'


def owner_delete(request, pk):
    try:
        Owner.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Owner is not found</h2>")


def owner_edit(request, pk):
    try:
        owner = Owner.objects.get(id=pk)
        form = OwnerForm(instance=owner)
    except Exception:
        return HttpResponseNotFound("<h2>Owner is not found</h2>")
    else:
        if request.method == 'POST':
            form = OwnerForm(request.POST, instance=owner)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        return render(request, 'owner_edit.html', context={'owner': pk, 'form': form})


# artist views
class ArtistView(ListView):
    model = Artist
    template_name = 'artist_page.html'
    queryset = Artist.objects.all()


class ArtistCreate(CreateView):
    model = Artist
    template_name = 'artist_form.html'
    form_class = ArtistForm
    success_url = '/'


def artist_delete(request, pk):
    try:
        Artist.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Artist is not found</h2>")


def artist_edit(request, pk):
    try:
        artist = Artist.objects.get(id=pk)
        form = ArtistForm(instance=artist)
    except Exception:
        return HttpResponseNotFound("<h2>Artist is not found</h2>")
    else:
        if request.method == 'POST':
            form = ArtistForm(request.POST, instance=artist)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        return render(request, 'artist_edit.html', context={'artist': pk, 'form': form})


# artwork views
class ArtworkView(ListView):
    model = Artwork
    template_name = 'artwork_page.html'
    queryset = Artwork.objects.all()


class ArtworkCreate(CreateView):
    model = Artwork
    template_name = 'artwork_form.html'
    form_class = ArtworkForm
    success_url = '/'


def artwork_delete(request, pk):
    try:
        Artwork.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Artwork is not found</h2>")


def artwork_edit(request, pk):
    try:
        artwork = Artwork.objects.get(id=pk)
        form = ArtworkForm(instance=artwork)
    except Exception:
        return HttpResponseNotFound("<h2>Artwork is not found</h2>")
    else:
        if request.method == 'POST':
            form = ArtworkForm(request.POST, instance=artwork)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        return render(request, 'artwork_edit.html', context={'artwork': pk, 'form': form})


# exhibition views
class ExhibitionView(ListView):
    model = Exhibition
    template_name = 'exhibition_page.html'
    queryset = Exhibition.objects.all()


class ExhibitionCreate(CreateView):
    model = Exhibition
    template_name = 'exhibition_form.html'
    form_class = ExhibitionForm
    success_url = '/'


def exhibition_delete(request, pk):
    try:
        Exhibition.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Exhibition is not found</h2>")


def exhibition_edit(request, pk):
    try:
        exhibition = Exhibition.objects.get(id=pk)
        form = ArtworkForm(instance=exhibition)
    except Exception:
        return HttpResponseNotFound("<h2>Exhibition is not found</h2>")
    else:
        if request.method == 'POST':
            form = ExhibitionForm(request.POST, instance=exhibition)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        return render(request, 'exhibition_edit.html', context={'exhibition': pk, 'form': form})


# exhibition halls views
class ExhibitionHallView(ListView):
    model = ExhibitionHall
    template_name = 'exhibition_hall_page.html'
    queryset = ExhibitionHall.objects.all()


class ExhibitionHallCreate(CreateView):
    model = ExhibitionHall
    template_name = 'exhibition_hall_form.html'
    form_class = ExhibitionHallForm
    success_url = '/'


def exhibition_hall_delete(request, pk):
    try:
        ExhibitionHall.objects.get(id=pk).delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Exhibition hall is not found</h2>")


def exhibition_hall_edit(request, pk):
    try:
        exhibition_hall = ExhibitionHall.objects.get(id=pk)
        form = ArtworkForm(instance=exhibition_hall)
    except Exception:
        return HttpResponseNotFound("<h2>Exhibition hall is not found</h2>")
    else:
        if request.method == 'POST':
            form = ExhibitionHallForm(request.POST, instance=exhibition_hall)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        return render(request, 'exhibition_hall_edit.html', context={'exhibition_hall': pk, 'form': form})
