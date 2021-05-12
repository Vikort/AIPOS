from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import *


# Create your views here.
class OwnersApiView(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data, status=201)

    def delete(self, request, pk):
        owner = get_object_or_404(Owner.objects.all(), id=pk)
        print(owner)
        owner.delete()
        return Response({"message": "Owner with id `{}` has been deleted.".format(pk)
                         }, status=204)

    def put(self, request, pk):
        owner = get_object_or_404(Owner.objects.all(), id=pk)
        body = request.data
        serializer = OwnerSerializer(instance=owner, data=body, partial=True)
        owner = "Ok"
        if serializer.is_valid(raise_exception=True):
            owner = serializer.save()
        return Response({"owner": "Owner {} has been update".format(owner)})

    def post(self, request):
        print(request.data)
        serializer = OwnerSerializer(data=request.data)
        saved_info = "ok"
        if serializer.is_valid(raise_exception=True):
            saved_info = serializer.save()
        return Response({"success": "Owner '{}' created successfully".format(saved_info)})


class ArtistsApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=201)


class ArtworksApiView(APIView):
    def get(self, request):
        artwork = Artwork.objects.all()
        serializer = ArtworkSerializer(artwork, many=True)
        return Response(serializer.data, status=201)


class ExhibitionsApiView(APIView):
    def get(self, request):
        exhibitions = Exhibition.objects.all()
        serializer = ExhibitionSerializer(exhibitions, many=True)
        return Response(serializer.data, status=201)


class ExhibitionHallsApiView(APIView):
    def get(self, request):
        exhibition_halls = ExhibitionHall.objects.all()
        serializer = ExhibitionHallSerializer(exhibition_halls, many=True)
        return Response(serializer.data, status=201)
