import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from vision.forms import PhotoForm
from vision.gcv import render_doc_text
from vision.models import Photo


class PhotoView(View):
    def get(self, request, *args, **kwargs):
        photos = Photo.objects.all()
        context = {
            'form': PhotoForm(),
            'photos': photos,
        }
        return render(request, 'vision/photo.html', context)

    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            photos = Photo.objects.all()
            context = {
                'form': PhotoForm(),
                'photos': photos,
            }
            return render(request, 'vision/photo.html', context)
        photo = form.save()
        in_file = photo.photo.path
        out_file = os.path.join(settings.MEDIA_ROOT, 'output', str(photo.photo).split('/')[-1])
        render_doc_text(in_file, out_file)
        with open(out_file, 'rb') as image_file:
            content = image_file.read()
        photo.output = ContentFile(content, str(photo.photo).split('/')[-1])
        photo.save()
        return redirect('vision:photo-detail', photo.id)


class DetailView(View):
    def get(self, request, photo_id, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=photo_id)
        return render(request, 'vision/detail.html', {'photo': photo})


photo_view = PhotoView.as_view()
detail_view = DetailView.as_view()
