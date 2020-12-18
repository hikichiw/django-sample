from django.contrib import admin
from book.models import Book, BookStock, Publisher, Author

admin.site.register(Book)
admin.site.register(BookStock) # 追加
admin.site.register(Publisher) # 追加
admin.site.register(Author) # 追加
