from django.http import HttpResponse, request
from rest_framework.decorators import api_view
from posta.views import content
import os

'''This scrapper gets data from three on the best mentorship scrappers on the net'''
'''get access token from app and page id from the page'''

page_access_token = os.environ.get('MB_ACCESS_TOKEN')
facebook_page_id = os.environ.get('MB_PAGE_ID')
'''
purpose, load , load_item
'''
@api_view(['GET'])
def index(request):
    return HttpResponse('This is Mentor_Bot')

@api_view(['POST'])
def post_on_mb_page(request):
    page_access_token = str(request.POST.get('page_access_token'))
    facebook_page_id = str(request.POST.get('facebook_page_id'))
    if page_access_token and facebook_page_id:
        return(content(page_access_token, facebook_page_id, 'purpose', 'load ', 'load_item'))
    else:
        return HttpResponse('Add page access token and facebook page id')
