from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


def index(request):
    return JsonResponse({"message": "Hello, world!"}, status=status.HTTP_200_OK)
