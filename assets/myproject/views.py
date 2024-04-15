from django.http import HttpResponse
from django.shortcuts import render

# Define the homepage view
def homepage(request):
    #return HttpResponse('Welcome to my homepage!')
    return render(request, 'home.html')

# Define the about page view
def about(request):
    #return HttpResponse('Welcome to the about page!')
    return render(request, 'about.html')