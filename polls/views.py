from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.http.response import JsonResponse

from .models import Question


def index(request):
    list = Question.objects.all()
    result = serializers.serialize('python', list)
    return JsonResponse(result, safe=False)