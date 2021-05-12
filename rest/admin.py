from django.contrib import admin
from .models import Owner, ExhibitionHall, Exhibition, Artist, Artwork

# Register your models here.
admin.site.register(Owner)
admin.site.register(ExhibitionHall)
admin.site.register(Exhibition)
admin.site.register(Artwork)
admin.site.register(Artist)
