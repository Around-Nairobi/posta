from django.http import HttpResponse, request
from rest_framework.decorators import api_view
from posta.views import content
import os

'''This scrapper gets data from three on the best mentorship scrappers on the net'''
'''get access token from app and page id from the page'''

# page_access_token = os.environ.get('MB_ACCESS_TOKEN')
# facebook_page_id = os.environ.get('MB_PAGE_ID')

page_access_token = 'EAADZB7Q46ZCksBAFDJdKc4zW4yLTBNnefqFar7WHYJYZCbGFh0jzutTg78ZAwwyND6lQ2AmKrNMlLXAjlXHZAroQsOq0MUnujkKRDWkdahsurgsEall49Nx5vQh6KD0pYeyuJeVKVSz9hXvGydj284RQZBGvdg6H6CxHWUhsxn8liCugWYTOpjfNIfTG0ZAXZCjcp1sep9eZCDAZDZD'
facebook_page_id = '280294099451467'
app_secret = 'd745c3af46ebff89398fe51ea939a6bd'
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
      load_item='For all Math geniuses :)'
      link='www.projecteuler.net'
      return purpose, load, load_item

@api_view(['POST'])
def post_on_crowdie_page(request):
    '''sends formated posts to facebook page'''
    if page_access_token and facebook_page_id:
        purpose, load, load_item = sample_request()
        # print(purpose, load, load_item)
        return(content(page_access_token, facebook_page_id, app_secret, purpose, load, load_item))
    else:
        return HttpResponse('Add page access token and facebook page id')
