import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from djangorestapi.mixins import JsonResponseMixin


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
            "content": "JsonCBV.get",
        }
        return self.render_to_json_response(data)
