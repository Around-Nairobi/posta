from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests
import time
from .models import errors

@api_view(['GET'])
def index(request):
    if request:
      return HttpResponse("funtimes")


@api_view(['POST'])
def facebook_graph_call(request):
    """
    This should cater for all end points
    https://graph.facebook.com/{your-page-id}/feed?message=Hello%20world!&access_token={your-page-access-token}
    """
    page_access_token = request.GET.get('page_access_token')
    facebook_page_id = request.GET.get('facebook_page_id')

    if page_access_token and facebook_page_id:
        try:
          purpose = request.GET.get('purpose') #can be feed, photos, videos,
          load = request.GET.get('load') #can be message, url, link, source, published etc
          load_item = request.GET.get('load_item') #is the item you want posted eg Awesome!
          if purpose and load and load_item:
              graph = 'https://graph.facebook.com/'
              url = "{}{}{}{}{}{}{}{}{}{}{}{}".format(graph,facebook_page_id, '/', purpose, '?', load,'=',load_item, '&', 'access_token', '=', page_access_token)
              r = requests.post(url)
              if 'error' in r:
                return HttpResponse('this is not good')
              else:
                return HttpResponse(r)
          else:
              return HttpResponse('Not Found', status=404)
        except requests.ConnectionError:
          return("failed to connect")
    else:
          return HttpResponse('Bad Request', status=400)

def content(page_access_token, facebook_page_id, purpose, load , load_item):
    '''call this function and pass all the content you need to pass'''
    data = {
      "page_access_token": page_access_token,
      "facebook_page_id": facebook_page_id,
      "purpose": purpose,
      "load": load,
      "load_item": load_item
    }
    return requests.post('https://aroundnairobi.herokuapp.com/posta/facebook_graph_call', data)

def runner():
    '''This runner is called by a cron job on heroku that is triggered at certain times of the day
       It does the simple duty of calling the functions.
    '''
    pass

@api_view(['GET'])
def privacypolicy(request):
    return render(request, 'termsfeed-privacy-policy-html.html')

@api_view(['GET'])
def termsservice(request):
    return render(request, 'termsfeed-terms-service-html.html')
