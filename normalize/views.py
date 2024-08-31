from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from . import scripts


@api_view(['POST'])
def normalize_json(request):
    try:
        data = request.data
        url = data['url']
        output = scripts.normalizer(url)
        return Response(output, status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
