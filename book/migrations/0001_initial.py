# Generated by Django 2.2.16 on 2020-09-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('quantity', models.IntegerField(default=0, verbose_name='在庫数')),
                ('publisher', models.CharField(max_length=255, verbose_name='出版社')),
                ('author', models.CharField(max_length=255, verbose_name='著者')),
                ('summary', models.CharField(max_length=255, verbose_name='概要')),
            ],
        ),
    ]
