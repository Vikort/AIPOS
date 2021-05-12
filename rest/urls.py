from django.urls import path
from .views import *

urlpatterns = [
    path('owners', OwnersApiView.as_view(), name='owners'),
    path('artists', ArtistsApiView.as_view(), name='artists'),
    path('artworks', ArtworksApiView.as_view(), name='artworks'),
    path('exhibitions', ExhibitionsApiView.as_view(), name='exhibitions'),
    path('exhibition_halls', ExhibitionHallsApiView.as_view(), name='exhibition_halls'),
    path('owners/<int:pk>', OwnersApiView.as_view(),),
    path('artists/<int:pk>', ArtistsApiView.as_view(),),
    path('artworks/<int:pk>', ArtworksApiView.as_view(),),
    path('exhibitions/<int:pk>', ExhibitionsApiView.as_view()),
    path('exhibition_halls/<int:pk>', ExhibitionHallsApiView.as_view(),),
]
