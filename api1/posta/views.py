import os
import facebook
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests
import time
from .models import errors

facebook_graph_call_url = os.environ.get('facebook_graph_call_url')



@api_view(['GET'])
def index(request):
    if request:
      return HttpResponse("This is posta")

def generate_token(app_secret, page_id, access_token):
    access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(page_id, app_secret, access_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    print(access_token_info)
    return access_token_info['access_token']



@api_view(['POST'])
def facebook_graph_call(request):
    """
    This should cater for all end points
    https://graph.facebook.com/{your-page-id}/feed?message=Hello%20world!&access_token={your-page-access-token}
    """
    page_access_token = str(request.POST.get('page_access_token'))
    facebook_page_id = str(request.POST.get('facebook_page_id'))
    app_secret = str(request.POST.get('app_secret'))

    if page_access_token and facebook_page_id:
        try:
          user_long_token = generate_token(app_secret, facebook_page_id, page_access_token)
          graph = facebook.GraphAPI(access_token=user_long_token, version="3.1")
          pages_data = graph.get_object("/me/accounts")
          for item in pages_data['data']:
              if item['id'] == facebook_page_id:
                  page_access_token = item['access_token']

          purpose = str(request.POST.get('purpose') )#can be feed, photos, videos,
          load = str(request.POST.get('load')) #can be message, url, link, source, published etc
          load_item = str(request.POST.get('load_item')) #is the item you want posted eg Awesome!
          if purpose and load and load_item:
              graph = 'https://graph.facebook.com/'
              url = "{}{}{}{}{}{}{}{}{}{}{}{}".format(graph,facebook_page_id, '/', purpose, '?', load,'=',load_item, '&', 'access_token', '=', user_long_token)
              r = requests.post(url)
              if 'error' in r:
                return HttpResponse('this is not good', url)
              else:
                return HttpResponse(r,url,  status=200)
          else:
              return HttpResponse('Not Found', status=404)
        except requests.ConnectionError:
          return("failed to connect")
    else:
          return HttpResponse('Bad Request', page_access_token, facebook_page_id, status=400)

def content(page_access_token, facebook_page_id,app_secret, purpose, load , load_item):
    '''call this function and pass all the content you need to pass'''
    data = {
      "page_access_token": page_access_token,
      "facebook_page_id": facebook_page_id,
      "app_secret": app_secret,
      "purpose": purpose,
      "load": load,
      "load_item": load_item
    }
    # return requests.post(facebook_graph_call, data)
    response = requests.post('https://posta-ke.herokuapp.com/facebook_graph_call', data)
    return HttpResponse(response)

@api_view(['GET'])
def runner(request):
    '''This runner is called by a cron job on heroku that is triggered at certain times of the day
       It does the simple duty of calling the functions.
    '''
    # domain_url = os.environ.get('domain_url')
    domain_url = 'https://posta-ke.herokuapp.com/'
    # urls = ['posta/crowdie', 'posta/hschool']
    urls = os.environ.get('urls')

    for x in urls:
      trigger = ('{}'.format(domain_url + x))
      print('trigger', trigger)
      requests.get(x)
      return


@api_view(['GET'])
def privacypolicy(request):
    return render(request, 'termsfeed-privacy-policy-html.html')

@api_view(['GET'])
def termsservice(request):
    return render(request, 'termsfeed-terms-service-html.html')
