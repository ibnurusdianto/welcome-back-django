# jangan lupa import HttpResponse untuk membuat response
from django.http import HttpResponse

# jangan lupa import render untuk membuat response dari template
from django.shortcuts import render


# contoh membuat view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')