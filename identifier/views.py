from django.http import HttpResponse

# REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import Http404


@api_view(['GET', 'POST'])
def api_identifier(request, note_id):
    if request.method == 'POST':
        pass


def index(request):
    return render(request, 'identifier/index.html')