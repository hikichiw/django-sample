from django.contrib import admin

from vision.models import Image, ImageLabel

admin.site.register(Image)
admin.site.register(ImageLabel)
