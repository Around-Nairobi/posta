from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#       if request.GET:
#         message = 'lol'
#       else:
#         message = 'You submitted nothing!'
#       return message

@api_view(['GET'])
def index(request):
    if request:
      return HttpResponse("funtimes")

@api_view(['POST'])
def facebook_pages(request):
    return HttpResponse("facebook pages")
