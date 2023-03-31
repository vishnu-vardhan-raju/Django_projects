from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'expensis/index.html')

def add_expensis(request):
    return render(request, 'expensis/index.html')