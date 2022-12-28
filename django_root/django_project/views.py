from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test


def Home(request):
    return render(request,'home.html')