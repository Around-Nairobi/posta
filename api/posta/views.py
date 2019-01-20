from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    if request:
      return HttpResponse("funtimes")

@api_view(['POST'])
def facebook_pages(request):
    page_access_token = "YOUR TOKEN GOES HERE"
    facebook_page_id = "67509909999999"
    graph = 'https://graph.facebook.com/'
    return HttpResponse(graph + facebook_page_id + '/' + 'accounts?', "feed", message='test message' + page_access_token)
