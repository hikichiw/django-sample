from django.db import models

class Publisher(models.Model):
    name = models.CharField(verbose_name='出版社名', max_length=255)

class Author(models.Model):
    name = models.CharField(verbose_name='著者名', max_length=255)

class Book(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=255)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name='著者', max_length=255)
    summary = models.CharField(verbose_name='概要', max_length=255)

class BookStock(models.Model):
    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(verbose_name='在庫数', default=0)

