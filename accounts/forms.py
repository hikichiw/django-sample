from django.contrib.auth.forms import UsernameField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    username = UsernameField(label='ユーザ名', max_length=255)
    password = forms.CharField(label='パスワード', strip=False, widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_cache = None

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError('3文字以上で入力してください。')
        return username

    def clean(self):
        if not self.errors:
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                # ユーザ名を間違えているが、一般的にはセキュリティの観点から
                # ユーザ名、パスワードのどちらが間違っているかは画面に表示しない
                raise forms.ValidationError('ユーザ名またはパスワードが間違っています。')
            # パスワードはハッシュ化されているので平文での検索はできない
            if not user.check_password(password):
                # こちらもパスワードを間違えているが、ユーザ名と同様
                raise forms.ValidationError('ユーザ名またはパスワードが間違っています。')
            self.user_cache = user

    def get_user(self):
        return self.user_cache
