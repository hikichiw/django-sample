from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Image(models.Model):
    """ 画像モデル """
    title = models.CharField(verbose_name='タイトル', max_length=255)
    input_file = models.ImageField(verbose_name='入力ファイル', upload_to='images/')
    output_file = models.ImageField(verbose_name='出力ファイル', blank=True, null=True, upload_to='output/images/')
    text = models.TextField(verbose_name='テキスト', blank=True, null=True)
    thumbnail = ImageSpecField(source='input_file', processors=[ResizeToFill(250, 250)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.title


class ImageLabel(models.Model):
    """ 画像ラベルモデル """
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='labels')
    label = models.CharField(verbose_name='ラベル', max_length=255)
    score = models.DecimalField(verbose_name='スコア', max_digits=5, decimal_places=3)

    def __str__(self):
        return f'{self.label}({self.score})'
