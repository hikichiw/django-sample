from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView
from book.models import Book

class BookListView(ListView):
    model = Book

class BookDetailView(View):
    def get(self, request, book_id, *args, **kwargs):
        book = Book.objects.get(pk=book_id)
        context = {
            'book': book,
        }
        return render(request, 'book/book_detail.html', context)

# 追加
class IndexView(TemplateView):
    template_name = 'index.html'

book_list = BookListView.as_view()
book_detail = BookDetailView.as_view()
index = IndexView.as_view() # 追加
