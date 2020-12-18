from django.urls import path
from book import views

app_name = 'book'
urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('<int:book_id>', views.book_detail, name='book-detail'), # 追加
]
