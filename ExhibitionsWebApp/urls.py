from django.urls import path
from ExhibitionsWebApp.views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('owners_page', owners_view, name='owners_page'),
    path('owner_page/<int:pk>', owner_view, name='owner_page'),
    path('create_owner', owner_create, name='create_owner'),
    path("delete_owner/<int:pk>/", owner_delete, name="delete_owner"),
    path("edit_owner/<int:pk>/", owner_edit, name="edit_owner"),
    path('artists_page', artists_view, name='artists_page'),
    path('artist_page/<int:pk>', artist_view, name='artist_page'),
    path('create_artist', artist_create, name='create_artist'),
    path("delete_artist/<int:pk>/", artist_delete, name="delete_artist"),
    path("edit_artist/<int:pk>/", artist_edit, name="edit_artist"),
    path('artworks_page', artworks_view, name='artworks_page'),
    path('artwork_page/<int:pk>', artwork_view, name='artwork_page'),
    path('create_artwork', artwork_create, name='create_artwork'),
    path("delete_artwork/<int:pk>/", artwork_delete, name="delete_artwork"),
    path("edit_artwork/<int:pk>/", artwork_edit, name="edit_artwork"),
    path('exhibitions_page', exhibitions_view, name='exhibitions_page'),
    path('exhibition_page/<int:pk>', exhibition_view, name='exhibition_page'),
    path('create_exhibition', exhibition_create, name='create_exhibition'),
    path("delete_exhibition/<int:pk>/", exhibition_delete, name="delete_exhibition"),
    path("edit_exhibition/<int:pk>/", exhibition_edit, name="edit_exhibition"),
    path('exhibition_halls_page', exhibition_halls_view, name='exhibition_halls_page'),
    path('exhibition_hall_page/<int:pk>', exhibition_hall_view, name='exhibition_hall_page'),
    path('create_exhibition_hall', exhibition_hall_create, name='create_exhibition_hall'),
    path("delete_exhibition_hall/<int:pk>/", exhibition_hall_delete, name="delete_exhibition_hall"),
    path("edit_exhibition_hall/<int:pk>/", exhibition_hall_edit, name="edit_exhibition_hall"),
]
