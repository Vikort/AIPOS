from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='owners/', default=None, null=True, blank=True)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    place_of_birth = models.TextField()
    date_of_birth = models.DateField()
    biography = models.TextField()
    education = models.TextField()
    image = models.ImageField(upload_to='artists/', default=None, null=True, blank=True)


class Artwork(models.Model):
    name = models.CharField(max_length=100)
    kind_of_work = models.TextField()
    date = models.DateField()
    height = models.FloatField()
    width = models.FloatField()
    volume = models.FloatField()
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=int)
    image = models.ImageField(upload_to='artworks/', default=None, null=True, blank=True)


class Exhibition(models.Model):
    name = models.CharField(max_length=100)
    kind = models.TextField()
    date = models.DateTimeField()
    artworks = models.ManyToManyField(Artwork)
    description = models.TextField()
    image = models.ImageField(upload_to='exhibitions/', default=None, null=True, blank=True)

    def get_artworks(self):
        return [a for a in self.artworks.all()]


class ExhibitionHall(models.Model):
    name = models.CharField(max_length=100)
    square = models.FloatField()
    address = models.TextField()
    phone = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    description = models.TextField()
    exhibitions = models.ManyToManyField(Exhibition)
    image = models.ImageField(upload_to='exhibitionHalls/', default=None, null=True, blank=True)

    def get_exhibitions(self):
        return [e for e in self.exhibitions.all()]
