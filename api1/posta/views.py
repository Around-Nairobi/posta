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
          purpose = str(request.POST.get('purpose') )#can be feed, photos, videos,
          load = str(request.POST.get('load')) #can be message, url, link, source, published etc
          load_item = str(request.POST.get('load_item')) #is the item you want posted eg Awesome!
          link = str(request.POST.get('link')) #link to article

          if purpose and load and load_item:
              graph = 'https://graph.facebook.com/v3.3/'
              url = "{}{}{}{}{}{}{}{}{}{}{}{}".format(graph,facebook_page_id, '/', purpose, '?', load,'=',load_item, '&', 'link', '=',link, '&', 'access_token', '=', page_access_token)
              r = requests.post(url)
              # print('r', vars(r))
              # for key, value in r.items():
              #   if key is 'error':
              # return HttpResponse('this is not good', value)
              # else:
              return HttpResponse(r, status=200)
          else:
              return HttpResponse('Not Found', status=404)
        except requests.ConnectionError:
          return("failed to connect")
    else:
          return HttpResponse('Bad Request', page_access_token, facebook_page_id, status=400)

def content(page_access_token, facebook_page_id,app_secret, purpose, load , load_item, link):
    '''call this function and pass all the content you need to pass'''
    data = {
      "page_access_token": page_access_token,
      "facebook_page_id": facebook_page_id,
      "app_secret": app_secret,
      "purpose": purpose,
      "load": load,
      "load_item": load_item,
      "link": link
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
                  data = {}
                  data[typ]=msg
                  print('data', data)

                  email_subject = msg['subject']
                  email_from = msg['from']
                  date = msg['Date']

                  page = return_page(email_from)
                  print('page', page, email_from)
                  if page is not None:
                        content = {}
                        content[email_from]= email_subject
                        response = requests.post('{}{}{}{}'.format(domain_url, 'post_on_', page, '_page'))
                        return HttpResponse(response)
                  else:
                    return HttpResponse('Nonetype Error')
      # except Exception as e:
      #   print('error', e)


def return_page(email_from):
      for key, value in pages.items():
            for email in value:
                if email_from is email:
                    print('ef', email_from, key)
                    return key
                else:
                    return None
