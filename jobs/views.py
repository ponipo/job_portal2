# jobs/views.py

from django.shortcuts import render
from django.conf import settings
import requests

def job_list(request):
    query = request.GET.get('q', '')
    url = f"{settings.SUPABASE_URL}/rest/v1/jobs"
    headers = {
        "apikey": settings.SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_ANON_KEY}",
        "Content-Type": "application/json"
    }

    if query:
        # ilike.*keyword* で部分一致
        params = {
            "select": "*",
            "title": f"ilike.*{query}*"
        }
    else:
        # クエリがない場合でも select="*" は必須
        params = {
            "select": "*"
        }

    response = requests.get(url, headers=headers, params=params)
    jobs = response.json() if response.status_code == 200 else []
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})


def job_detail(request, job_id):
    url = f"{settings.SUPABASE_URL}/rest/v1/jobs"
    headers = {
        "apikey": settings.SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_ANON_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "select": "*",
        "id": f"eq.{job_id}"
    }

    response = requests.get(url, headers=headers, params=params)
    job_list = response.json() if response.status_code == 200 else []
    job = job_list[0] if job_list else None
    return render(request, 'jobs/job_detail.html', {'job': job})
