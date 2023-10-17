from django.shortcuts import render

def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')
