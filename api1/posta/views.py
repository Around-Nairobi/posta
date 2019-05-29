import os
import facebook
import smtplib
import time
import imaplib
import email
import struct
import re, datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests
import time
from .models import errors
from .emails import pages

facebook_graph_call_url = os.environ.get('facebook_graph_call_url')
domain_url = os.environ.get('domain_url')
endpoints = [
            "{}{}".format(domain_url,'post_on_crowdie_page'),
            "{}{}".format(domain_url,'post_on_mb_page'),
            "{}{}".format(domain_url,'post_on_msafiri_page'),
            "{}{}".format(domain_url,'post_on_tbtia_page'),
            "{}{}".format(domain_url,'post_on_tm_page'),
            "{}{}".format(domain_url,'post_on_hschool_page')
             ]

@api_view(['GET'])
def index(request):
    if request:
      for endpoint in endpoints:
        response = requests.post(endpoint)
        send_to_email=[]
        send_to_email.append(response)
        return HttpResponse("This is posta", send_to_email)

def generate_token(app_secret, page_id, access_token):
    access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(page_id, app_secret, access_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    print(access_token_info)
    try:
        return access_token_info['access_token']
    except KeyError:
        return access_token_info



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
          # user_long_token = generate_token(app_secret, facebook_page_id, page_access_token)
          # user_long_token = "EAADZB7Q46ZCksBAJE9gyB7QTQn9Yi34cZAUbll2dUWzqHPyP0jQj1ZAk8cacXo2wwkdCLCvfycZBbzUp0otSBJ0WYYJbZAyh6H3mrmDkvYhyBohcxjYkZBHTZBR2GWQ3WTvGrZCW3MaWqVkJXk32vcZCrRDpH2AHIPZCyiZCvUAfq6gLS7IZAPDP7kDJPzUiFgKPrcVkZD"
          # graph = facebook.GraphAPI(access_token=user_long_token, version="3.1")
          # pages_data = graph.get_object("/me/accounts")
          # for item in pages_data['data']:
              # if item['id'] == facebook_page_id:
                  # page_access_token = item['access_token']
                  # page_access_token = page_access_token

          purpose = str(request.POST.get('purpose') )#can be feed, photos, videos,
          load = str(request.POST.get('load')) #can be message, url, link, source, published etc
          load_item = str(request.POST.get('load_item')) #is the item you want posted eg Awesome!


          if purpose and load and load_item:
              # graph = facebook.GraphAPI(access_token=page_access_token, version="3.1")
              # r = graph.post(id=facebook_page_id,
                                            # field = purpose,
                                            # load = load_item)

              graph = 'https://graph.facebook.com/'
              url = "{}{}{}{}{}{}{}{}{}{}{}{}".format(graph,facebook_page_id, '/', purpose, '?', load,'=',load_item, '&', 'access_token', '=', page_access_token)
              r = requests.post(url)
              if 'error' in r:
                return HttpResponse('this is not good')
              else:
                return HttpResponse(r, status=200)
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
    response = requests.post('https://posta-ke.herokuapp.com/facebook_graph_call', data)
    return HttpResponse(response)

@api_view(['GET'])
def privacypolicy(request):
    return render(request, 'termsfeed-privacy-policy-html.html')

@api_view(['GET'])
def termsservice(request):
    return render(request, 'termsfeed-terms-service-html.html')

FROM_EMAIL  = os.environ.get('FROM_EMAIL')
FROM_PWD    = os.environ.get('FROM_PWD')
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

@api_view(['GET'])
def read_email_from_gmail(request):
      '''Utility to read email from Gmail Using Python
      https://docs.python.org/3/library/email.parser.html
      https://docs.python.org/3/library/imaplib.html'''

      # try:
      mail = imaplib.IMAP4_SSL(SMTP_SERVER)
      mail.login(FROM_EMAIL,FROM_PWD)
      mail.select('inbox')

      types, data = mail.search(None, 'ALL')
      mail_ids = data[0]

      id_list = mail_ids.split()
      first_email_id = int(id_list[0])
      latest_email_id = int(id_list[-1])

      for i in range(latest_email_id,first_email_id, -1):
          typ, data = mail.fetch(str(i), '(RFC822)' )

          for response_part in data:
              if isinstance(response_part, tuple):
                  msg = email.message_from_bytes(response_part[1])

                  email_subject = msg['subject']
                  email_from = msg['from']
                  date = msg['Date']


                  content = {}
                  content[email_from]= email_subject
                  print('date', date)
                  print('from', email_from)
                  # print('msg', msg)
                  page = return_page(email_from)
                  if page:
                        response = requests.post('{}{}{}{}'.format(domain_url, 'post_on_', page, 'page'))
                        return HttpResponse(response)
                  # print('From : ' + email_from + '\n')
                  # print('Subject : ' + email_subject + '\n')
      # except Exception as e:
      #   print('error', e)


def return_page(email_from):
      for key, value in pages.items():
            if email_from in value:
              return key
            else:
                  return "error"
