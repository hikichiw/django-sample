from django.urls import path

from vision import views

app_name = 'vision'
urlpatterns = [
    path('', views.vision_view, name='vision'),
    path('image/<int:image_id>', views.image_view, name='image'),
]
