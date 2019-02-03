import json
from django.views.generic import View
from django.http import HttpResponse

from djangorestapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from updates.models import Update as UpdateModel


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "Unknown data"})
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You can't delete entire list."})
        return self.render_to_response(data, status=403)


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data, status=403)
