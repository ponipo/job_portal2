# job_portal/settings.py

import os
from pathlib import Path

# プロジェクトのベースディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティキー（開発用）
SECRET_KEY = 'your-secret-key'

# デバッグモード
DEBUG = True

ALLOWED_HOSTS = ['job-portal2-yax9.onrender.com']


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

# SupabaseのURLとキー設定
SUPABASE_URL = "https://ryxveuvpzjmkynykcass.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ5eHZldXZwempta3lueWtjYXNzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM3MTcyMDAsImV4cCI6MjA0OTI5MzIwMH0.NhwizsYCoqcRBWlHYi0w4wN8ttc5GczwCzpl8wayq38"  # 必ずあなたのAnonキーに置き換えてください
