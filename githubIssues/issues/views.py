# from django.shortcuts import render
# Create your views here.
from .models import Board
from django.shortcuts import render
from Scripts import extract_issues, config
import json


default_repo = '1272371/github-issues'


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def issues(request):
    repo_name = default_repo
    access_token = config.get_access_token()
    all_issues = extract_issues.from_project(access_token, repo_name)
    return render(request, 'issues.html', {'issues': json.dumps(all_issues)})
