from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

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
    path('token/obtain', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register', CreateUser.as_view(), name="create_user"),
    path('logout', LogoutUser.as_view(), name="logout_user"),
]
