from django.shortcuts import render

# Create your views here.
def get_home(req):
    return render(req, 'home.html')