# jobs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # 求人一覧
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),  # 求人詳細
]
