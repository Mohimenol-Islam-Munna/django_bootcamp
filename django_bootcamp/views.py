from django.http import HttpResponse 


def home(request):
    return HttpResponse("This is our home page")


def about(request):
    return HttpResponse("This is our about page")


def contact(request):
    return HttpResponse("This is our contact page")