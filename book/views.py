from django.shortcuts import render
from django.views.generic.base import View

from book.models import Book


class BookListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        context = {
            'book_list': queryset,
        }
        return render(request, 'book/book_list.html', context)

book_list = BookListView.as_view()
