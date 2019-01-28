from posta.views import content

'''This scrapper gets data from three on the best mentorship scrappers on the net'''
'''get access token from app and page id from the page'''

page_access_token = "mama"
facebook_page_id = "mama" ,
'''
purpose, load , load_item
'''
def index():
    return 'This is Mentor_Bot'

def scrapper_one():
    return(content(page_access_token, facebook_page_id, 'purpose', 'load ', 'load_item'))
    
