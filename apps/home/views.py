from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, "index.html", {"date": timezone.now()})
