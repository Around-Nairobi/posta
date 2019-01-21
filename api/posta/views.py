from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render

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
    try:
      page_access_token = request.GET.get('page_access_token')
      facebook_page_id = request.GET.get('facebook_page_id')
      purpose = request.GET.get('purpose') #can be feed, photos, videos,
      load = request.GET.get('load') #can be message, url, link, source, published etc
      load_item = request.GET.get('load_item') #is the item you want posted eg Awesome!
      graph = 'https://graph.facebook.com/'
      r = request.POST(graph + facebook_page_id + '/' + purpose + '?' + load=load_item + '&' + access_token=page_access_token)
      return HttpResponse(r)
    except request.ConnectionError:
      return("failed to connect")


@api_view(['GET'])
def privacypolicy(request):
    return render('Privacy Policy', 'posta/templates/termsfeed-privacy-policy-html.html')

@api_view(['GET'])
def termsservice(request):
    return render('Terms of Service', 'posta/templates/ttermsfeed-terms-service-html.html')
