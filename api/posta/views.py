from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view(['GET'])
def index(request):
    if request:
      return HttpResponse("funtimes")

@api_view(['POST'])
def facebook_pages(request):
    try:
      page_access_token = request.GET.get('page_access_token')
      facebook_page_id = request.GET.get('facebook_page_id')
      message = request.GET.get('message')
      graph = 'https://graph.facebook.com/'
      r = request.POST(graph + facebook_page_id + '/' + 'feed' + message + '/' + page_access_token)
      return HttpResponse(r)
    except request.ConnectionError:
      return("failed to connect")


@api_view(['GET'])
def privacypolicy(request):
    return render('Privacy Policy', 'templates/termsfeed-privacy-policy-html.html')

@api_view(['GET'])
def termsservice(request):
    return render('Terms of Service', 'templates/ttermsfeed-terms-service-html.html')
