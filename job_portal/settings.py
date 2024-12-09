# job_portal/settings.py

import os
from pathlib import Path

# プロジェクトのベースディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティキー（開発用）
SECRET_KEY = 'your-secret-key'

# デバッグモード
DEBUG = True

ALLOWED_HOSTS = []

# アプリケーション定義
INSTALLED_APPS = [
    'jobs',  # 追加
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # 追加
    'django.contrib.staticfiles',
]

# ミドルウェア
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 追加開始
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # ここを追加
    # 追加終了
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'job_portal.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 追加
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # コンテキストプロセッサ
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 追加開始
                'django.contrib.auth.context_processors.auth',      # ここを追加
                'django.contrib.messages.context_processors.messages',  # ここを追加
                # 追加終了
            ],
        },
    },
]

WSGI_APPLICATION = 'job_portal.wsgi.application'

# データベース設定（今回は使用しない）
DATABASES = {}

# 静的ファイルのURL
STATIC_URL = '/static/'

# 静的ファイルのディレクトリ（必要に応じて）
STATICFILES_DIRS = [BASE_DIR / 'static']

# 警告対応：STATICFILES_DIRSで指定したディレクトリが存在するか確認
# 存在しない場合は、staticフォルダを作成するか、以下の行をコメントアウト
# STATICFILES_DIRS = [BASE_DIR / 'static']
