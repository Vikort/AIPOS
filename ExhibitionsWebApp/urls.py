from django.urls import path
from ExhibitionsWebApp.views import *

urlpatterns = [
    path('', main_page),
    path('owner_page', OwnerView.as_view(), name='owner_page'),
    path('create_owner', OwnerCreate.as_view(), name='create_owner'),
    path("delete_owner/<int:pk>/", owner_delete, name="delete_owner"),
    path("edit_owner/<int:pk>/", owner_edit, name="edit_owner"),
    path('artist_page', ArtistView.as_view(), name='artist_page'),
    path('create_artist', ArtistCreate.as_view(), name='create_artist'),
    path("delete_artist/<int:pk>/", artist_delete, name="delete_artist"),
    path("edit_artist/<int:pk>/", artist_edit, name="edit_artist"),
    path('artwork_page', ArtworkView.as_view(), name='artwork_page'),
    path('create_artwork', ArtworkCreate.as_view(), name='create_artwork'),
    path("delete_artwork/<int:pk>/", artwork_delete, name="delete_artwork"),
    path("edit_artwork/<int:pk>/", artwork_edit, name="edit_artwork"),
    path('exhibition_page', ExhibitionView.as_view(), name='exhibition_page'),
    path('create_exhibition', ExhibitionCreate.as_view(), name='create_exhibition'),
    path("delete_exhibition/<int:pk>/", exhibition_delete, name="delete_exhibition"),
    path("edit_exhibition/<int:pk>/", exhibition_edit, name="edit_exhibition"),
    path('exhibition_hall_page', ExhibitionHallView.as_view(), name='exhibition_hall_page'),
    path('create_exhibition_hall', ExhibitionHallCreate.as_view(), name='create_exhibition_hall'),
    path("delete_exhibition_hall/<int:pk>/", exhibition_hall_delete, name="delete_exhibition_hall"),
    path("edit_exhibition_hall/<int:pk>/", exhibition_hall_edit, name="edit_exhibition_hall"),
]
