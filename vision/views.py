from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from vision.forms import ImageForm
from vision.gcv import analyze_img
from vision.models import Image, ImageLabel


class VisionView(View):
    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        context = {
            'form': ImageForm(),
            'images': images,
        }
        return render(request, 'vision/vision.html', context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if not form.is_valid():
            images = Image.objects.all()
            context = {
                'form': ImageForm(),
                'images': images,
            }
            return render(request, 'vision/vision.html', context)
        image = form.save()
        in_file = image.input_file.path
        labels, texts, out_image = analyze_img(in_file)
        for label, score in labels:
            image_label = ImageLabel(image=image, label=label, score=score)
            image_label.save()
        image.text = texts
        image.output_file = ContentFile(out_image, str(image.input_file).split('/')[-1])
        image.save()
        return redirect('vision:image', image.id)


class ImageView(View):
    def get(self, request, image_id, *args, **kwargs):
        image = get_object_or_404(Image, pk=image_id)
        return render(request, 'vision/image.html', {'image': image})


vision_view = VisionView.as_view()
image_view = ImageView.as_view()
