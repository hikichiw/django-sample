from django.contrib.auth.forms import UsernameField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from vision.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'photo')
