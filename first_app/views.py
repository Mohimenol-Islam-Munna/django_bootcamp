from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee(request):
    return HttpResponse('first_app employee')

def employee_list(request):
    return HttpResponse('first_app employee list')
