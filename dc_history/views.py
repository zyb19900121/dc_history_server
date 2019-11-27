from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.http.response import JsonResponse
import json

from .models import Dynasty


def formatResponse(list, total):
    result = {'status_code': "8888",
              'data': serializers.serialize('python', list),
              "total": total}
    return result


def index(request):
    return HttpResponse("DC_History server启动成功！")


def getDynastyList(request):
    if(request.method == 'GET'):
        try:
            currentPage = int(request.GET.get('currentPage')) or 1
            pageSize = int(request.GET.get('pageSize')) or 10
            offset = (currentPage - 1) * pageSize
            limit = offset + pageSize
            dynastyList = Dynasty.objects.all().order_by(
                'dynasty_order', '-date_update')[offset:limit]
            total = Dynasty.objects.count()
            result = formatResponse(dynastyList, total)
        except Exception as e:
            status_code = "0000"
            msg = str(e)
            result = {"status_code": status_code, "msg": msg}
        finally:
            return JsonResponse(result, safe=False)


def saveDynasty(request):
    if(request.method == 'POST'):
        status_code = "8888"
        msg = "success"
        try:
            newDynasty = Dynasty(**json.loads(request.body))
            newDynasty.save()
        except Exception as e:
            status_code = "0000"
            msg = str(e)
        finally:
            result = {"status_code": status_code, "msg": msg}
            return HttpResponse(json.dumps(result))


def removeDynasty(request):
    if(request.method == "POST"):
        status_code = "8888"
        msg = "success"
        try:
            ids = json.loads(request.body)["ids"]
            for id in ids:
                Dynasty.objects.filter(id=id).delete()
                pass
        except Exception as e:
            status_code = "0000"
            msg = str(e)
        finally:
            result = {"status_code": status_code, "msg": msg}
            return HttpResponse(json.dumps(result))
