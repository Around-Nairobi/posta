from django.http import HttpResponse, request
from rest_framework.decorators import api_view
from posta.views import content
import os

'''This scrapper gets data from three on the best mentorship scrappers on the net'''
'''get access token from app and page id from the page'''

page_access_token = os.environ.get('CROWDIE_ACCESS_TOKEN')
facebook_page_id = os.environ.get('CROWDIE_PAGE_ID')
app_secret = os.environ.get('CROWDIE_APP_SECRET')

'''
purpose, load , load_item
'''
@api_view(['GET'])
def index(request):
    return HttpResponse('This is Crowdie')

def scrapper():
      '''scraps data from websites and formats it'''
      '''purpose can be: feed, picture etc'''
      data = {
        "purpose": "feed",
        "load": "load",
        "load_item": "load_item"
      }
      return data

def sample_request():
      purpose='feed'
      load='message'
      load_item='Rahman'
      link='www.projecteuler.net'
      return purpose, load, load_item

@api_view(['POST'])
def post_on_crowdie_page(request):
    '''sends formated posts to facebook page'''
    if page_access_token and facebook_page_id:
        purpose, load, load_item = sample_request()
        return(content(page_access_token, facebook_page_id, app_secret, purpose, load, load_item))
    else:
        return HttpResponse('Add page access token and facebook page id')
