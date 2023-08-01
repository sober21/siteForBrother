from django.shortcuts import render


def index(request):
    return render(request, 'simplesite/index.html')


def second(request):
    return render(request, 'simplesite/second.html')