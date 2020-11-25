# Create your views here.
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Firt half, Second half, Climax"}
    return render(request, 'rango/index.html', context=context_dict)
