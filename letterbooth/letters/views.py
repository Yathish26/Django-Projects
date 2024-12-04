from django.shortcuts import render
from . models import Letter

def letter_list(request):
    letters = Letter.objects.all()
    return render(request, 'home.html', {'letters': letters})