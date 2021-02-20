from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Photo(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=255)
    photo = models.ImageField(verbose_name='フォト', upload_to='images/')
    output = models.ImageField(verbose_name='出力', blank=True, null=True, upload_to='output/images/')
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(250, 250)], format="JPEG",
                               options={'quality': 60})
