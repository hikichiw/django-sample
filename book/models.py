from django.db import models


class Book(models.Model):
    """本モデル"""
    title = models.CharField(verbose_name='タイトル', max_length=255)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)
    publisher = models.CharField(verbose_name='出版社', max_length=255)
    author = models.CharField(verbose_name='著者', max_length=255)
    summary = models.CharField(verbose_name='概要', max_length=255)
