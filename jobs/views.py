# jobs/views.py

from django.shortcuts import render
import pandas as pd
from django.conf import settings

# Excelファイルのパス
excel_file = settings.BASE_DIR / 'jobs.xlsx'

# データフレームを読み込む
df = pd.read_excel(excel_file)

def job_list(request):
    query = request.GET.get('q', '')
    if query:
        filtered_df = df[df['title'].str.contains(query, case=False, na=False)]
    else:
        filtered_df = df
    jobs = filtered_df.to_dict('records')
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})

def job_detail(request, job_id):
    job = df[df['id'] == job_id].to_dict('records')
    if job:
        job = job[0]
    else:
        job = None
    return render(request, 'jobs/job_detail.html', {'job': job})
