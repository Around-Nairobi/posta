from posta.views import content
import os

'''This scrapper gets data from three on the best mentorship scrappers on the net'''
'''get access token from app and page id from the page'''

page_access_token = os.environ.get('ACCESS_TOKEN')
facebook_page_id = os.environ.get('MB_PAGE_ID')
'''
purpose, load , load_item
'''
def index():
    return 'This is Mentor_Bot'

def get_twitter():
    return(content(page_access_token, facebook_page_id, 'purpose', 'load ', 'load_item'))
