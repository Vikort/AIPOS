from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound
import requests
import json

# Create your views here.

api_url = 'http://localhost:8000/rest_api/'


def main_page(request):
    return render(request, 'main_page.html', {})


# owner views
def owners_view(request):
    owners = requests.get(api_url + 'owners').json()
    return render(request, 'owners_page.html', context={'owner_list': owners})


def owner_view(request, pk):
    result = requests.get(api_url + "owners").json()
    owner = None
    for i in result:
        if i['id'] == pk:
            owner = i
    if owner is None:
        return HttpResponseNotFound('<h2>Owner is not found</h2>')
    return render(request, "owner_page.html", context={"owner": owner})


def owner_create(request):
    if request.method == "POST":
        payload = {
            'name': request.POST['name'],
            'address': request.POST['address'],
            'phone': request.POST['phone'],
            'description': request.POST['description'],
            # 'image': request.POST['image'],
        }
        status_code = requests.post(api_url + "owners", json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    return render(request, 'owner_form.html', {'form': OwnerForm})


def owner_delete(request, pk):
    answer = requests.delete(api_url + "owners/" + str(pk)).status_code
    return redirect('owners_page')


def owner_edit(request, pk):
    if request.method == "POST":
        payload = {
            'name': request.POST['name'],
            'address': request.POST['address'],
            'phone': request.POST['phone'],
            'description': request.POST['description'],
            # 'image': request.POST['image'],
        }
        status_code = requests.put(api_url + "owners/" + str(pk), json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    result = requests.get(api_url + "owners").json()
    owner = None
    for i in result:
        if i['id'] == pk:
            owner = i
    if owner is None:
        return HttpResponseNotFound('<h2>Owner is not found</h2>')
    return render(request, 'owner_edit.html', {'form': OwnerForm, 'owner': owner['id']})


# artist views
def artists_view(request):
    artists = requests.get(api_url + 'artists').json()
    return render(request, 'artists_page.html', context={'artist_list': artists})


def artist_view(request, pk):
    result = requests.get(api_url + "artists").json()
    artist = None
    for i in result:
        if i['id'] == pk:
            artist = i
    if artist is None:
        return HttpResponseNotFound('<h2>Artist is not found</h2>')
    return render(request, "artist_page.html", context={"artist": artist})


def artist_create(request):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "place_of_birth": request.POST['place_of_birth'],
            "date_of_birth": request.POST['date_of_birth'],
            "biography": request.POST['biography'],
            "education": request.POST['education'],
            # 'image': request.POST['image'],
        }
        status_code = requests.post(api_url + "artists", json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    return render(request, 'artist_form.html', {'form': ArtistForm})


def artist_delete(request, pk):
    answer = requests.delete(api_url + "artists/" + str(pk)).status_code
    return redirect('artists_page')


def artist_edit(request, pk):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "place_of_birth": request.POST['place_of_birth'],
            "date_of_birth": request.POST['date_of_birth'],
            "biography": request.POST['biography'],
            "education": request.POST['education'],
            # 'image': request.POST['image'],
        }
        status_code = requests.put(api_url + "artists/" + str(pk), json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    result = requests.get(api_url + "artists").json()
    artist = None
    for i in result:
        if i['id'] == pk:
            artist = i
    if artist is None:
        return HttpResponseNotFound('<h2>Artist is not found</h2>')
    return render(request, 'artist_edit.html', {'form': ArtistForm, 'artist': artist['id']})


# artwork views
def artworks_view(request):
    artworks = requests.get(api_url + 'artworks').json()
    return render(request, 'artworks_page.html', context={'artwork_list': artworks})


def artwork_view(request, pk):
    result = requests.get(api_url + "artworks").json()
    artwork = None
    for i in result:
        if i['id'] == pk:
            artwork = i
    if artwork is None:
        return HttpResponseNotFound('<h2>Artwork is not found</h2>')
    artists = requests.get(api_url + "artists").json()
    artist = None
    for i in artists:
        if i['id'] == artwork['artist']:
            artist = i
    artwork['artist_name'] = artist['name']
    return render(request, "artwork_page.html", context={"artwork": artwork})


def artwork_create(request):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "kind_of_work": request.POST['kind_of_work'],
            "date": request.POST['date'],
            "height": request.POST['height'],
            "width": request.POST['width'],
            "volume": request.POST['volume'],
            "description": request.POST['description'],
            "artist": request.POST['artist'],
            # 'image': request.POST['image'],
        }
        status_code = requests.post(api_url + "artworks", json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    return render(request, 'artwork_form.html', {'form': ArtworkForm})


def artwork_delete(request, pk):
    answer = requests.delete(api_url + "artworks/" + str(pk)).status_code
    return redirect('artworks_page')


def artwork_edit(request, pk):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "kind_of_work": request.POST['kind_of_work'],
            "date": request.POST['date'],
            "height": request.POST['height'],
            "width": request.POST['width'],
            "volume": request.POST['volume'],
            "description": request.POST['description'],
            "artist": request.POST['artist'],
            # 'image': request.POST['image'],
        }
        status_code = requests.put(api_url + "artworks/" + str(pk), json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    result = requests.get(api_url + "artworks").json()
    artwork = None
    for i in result:
        if i['id'] == pk:
            artwork = i
    if artwork is None:
        return HttpResponseNotFound('<h2>Artwork is not found</h2>')
    return render(request, 'artwork_edit.html', {'form': ArtworkForm, 'artwork': artwork['id']})


# exhibition views
def exhibitions_view(request):
    exhibitions = requests.get(api_url + 'exhibitions').json()
    return render(request, 'exhibitions_page.html', context={'exhibition_list': exhibitions})


def exhibition_view(request, pk):
    result = requests.get(api_url + "exhibitions").json()
    exhibition = None
    for i in result:
        if i['id'] == pk:
            exhibition = i
    if exhibition is None:
        return HttpResponseNotFound("<h2>Exhibition is not found</h2>")
    artworks = requests.get(api_url + "artworks").json()
    artworks_list = []
    for i in artworks:
        for j in exhibition['artworks']:
            if i['id'] == j:
                artworks_list.append(i)
    exhibition['artworks'] = artworks_list
    return render(request, "exhibition_page.html", context={"exhibition": exhibition})


def exhibition_create(request):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "kind": request.POST['kind'],
            "date": request.POST['date'],
            "description": request.POST['description'],
            "artworks": request.POST['artworks'],
            # 'image': request.POST['image'],
        }
        status_code = requests.post(api_url + "exhibitions", json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    return render(request, 'exhibition_form.html', {'form': ExhibitionForm})


def exhibition_delete(request, pk):
    answer = requests.delete(api_url + "exhibitions/" + str(pk)).status_code
    return redirect('exhibitions_page')


def exhibition_edit(request, pk):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "kind": request.POST['kind'],
            "date": request.POST['date'],
            "description": request.POST['description'],
            "artworks": request.POST['artworks'],
            # 'image': request.POST['image'],
        }
        status_code = requests.put(api_url + "exhibitions/" + str(pk), json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    result = requests.get(api_url + "exhibitions").json()
    exhibition = None
    for i in result:
        if i['id'] == pk:
            exhibition = i
    if exhibition is None:
        return HttpResponseNotFound("<h2>Exhibition is not found</h2>")
    return render(request, 'exhibition_edit.html', {'form': ExhibitionForm, 'exhibition': exhibition['id']})


# exhibition halls views
def exhibition_halls_view(request):
    exhibition_halls = requests.get(api_url + 'exhibition_halls').json()
    return render(request, 'exhibition_halls_page.html', context={'exhibition_hall_list': exhibition_halls})


def exhibition_hall_view(request, pk):
    result = requests.get(api_url + "exhibition_halls").json()
    exhibition_hall = None
    for i in result:
        if i['id'] == pk:
            exhibition_hall = i
    if exhibition_hall is None:
        return HttpResponseNotFound("<h2>Exhibition hall is not found</h2>")
    exhibitions = requests.get(api_url + "exhibitions").json()
    exhibitions_list = []
    for i in exhibitions:
        for j in exhibition_hall['exhibitions']:
            if i['id'] == j:
                exhibitions_list.append(i)
    exhibition_hall['exhibitions'] = exhibitions_list
    owners = requests.get(api_url + 'owners').json()
    for i in owners:
        if i['id'] == exhibition_hall['owner']:
            exhibition_hall['owner_name'] = i['name']
    return render(request, "exhibition_hall_page.html", context={"exhibition_hall": exhibition_hall})


def exhibition_hall_create(request):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "square": request.POST['kind'],
            "address": request.POST['date'],
            "phone": request.POST['phone'],
            "description": request.POST['description'],
            "owner": request.POST['owner'],
            "exhibitions": request.POST['exhibitions'],
            # 'image': request.POST['image'],
        }
        status_code = requests.post(api_url + "exhibition_halls", json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    return render(request, 'exhibition_hall_form.html', {'form': ExhibitionHallForm})


def exhibition_hall_delete(request, pk):
    answer = requests.delete(api_url + "exhibition_halls/" + str(pk)).status_code
    return redirect('exhibition_halls_page')


def exhibition_hall_edit(request, pk):
    if request.method == "POST":
        payload = {
            "name": request.POST['name'],
            "square": request.POST['kind'],
            "address": request.POST['date'],
            "phone": request.POST['phone'],
            "description": request.POST['description'],
            "owner": request.POST['owner'],
            "exhibitions": request.POST['exhibitions'],
            # 'image': request.POST['image'],
        }
        status_code = requests.put(api_url + "exhibition_halls/" + str(pk), json=payload)
        if status_code.status_code != 200:
            return HttpResponseNotFound(f"<h2>{status_code.text}</h2>")
        else:
            return HttpResponseRedirect('/')
    result = requests.get(api_url + "exhibition_halls").json()
    exhibition_hall = None
    for i in result:
        if i['id'] == pk:
            exhibition_hall = i
    if exhibition_hall is None:
        return HttpResponseNotFound("<h2>Exhibition hall is not found</h2>")
    return render(request, 'exhibition_hall_edit.html', {'form': ExhibitionHallForm, 'exhibitions_hall': exhibition_hall['id']})
