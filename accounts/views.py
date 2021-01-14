from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from accounts.forms import LoginForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'accounts/login.html', {'form': LoginForm()})

    def post(self, request, *args, **kwargs):
        # リクエストからフォームを作成
        form = LoginForm(request.POST)
        # バリデーション（ユーザーの認証も合わせて実施）
        if not form.is_valid():
            # バリデーションNGの場合はログイン画面のテンプレートを再表示
            return render(request, 'accounts/login.html', {'form': form})
        # ユーザーオブジェクトをフォームから取得
        user = form.get_user()
        # ログイン処理
        auth_login(request, user)
        # トップ画面にリダイレクト
        return redirect(reverse('index'))

login = LoginView.as_view()
