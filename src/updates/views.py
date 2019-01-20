import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from djangorestapi.mixins import JsonResponseMixin
from .models import Update


def json_example_view1(request):
    data = {
        "count": 1000,
        "content": "json_example_view1",
    }
    return JsonResponse(data)


def json_example_view2(request):
    data = {
        "count": 1000,
        "content": "json_example_view2",
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "JsonCBV.get",
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "JsonCBV2.get",
        }
        return self.render_to_json_response(data)


class SerializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            "user": obj.user.username,
            "content": obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Update.objects.all()
        data = serialize("json", queryset) #serialize("json", queryset, fields=('user', 'content'))
        print(data)
        # data = {
        #     "user": queryset.user.username,
        #     "content": queryset.content,
        # }
        # json_data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
