from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from django.conf import settings

def index(request):
    print(settings.BASE_DIR)
    return render(request, 'base.html', {
        'date': timezone.now() 
    })
    