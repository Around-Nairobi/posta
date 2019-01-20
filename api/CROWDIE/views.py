from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['GET'])
def index():
    return 'This is Crowdie'

@api_view(['POST'])
def post_crowdie():
    '''This posts messages to the crowdie page'''
    return 'funtimes'
