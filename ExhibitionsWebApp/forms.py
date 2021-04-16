from django import forms
from .models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'


class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'


class ExhibitionHallForm(forms.ModelForm):
    class Meta:
        model = ExhibitionHall
        fields = '__all__'
