from django.urls import path

from vision import views

app_name = 'vision'
urlpatterns = [
    path('photo', views.photo_view, name='photo'),
    path('photo/<int:photo_id>', views.detail_view, name='photo-detail'),
]
