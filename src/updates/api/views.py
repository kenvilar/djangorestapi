import json
from django.views.generic import View
from django.http import HttpResponse

from djangorestapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from .utils import is_json


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You can't delete entire list."})
        return self.render_to_response(data, status=403)


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        # return obj
        queryset = UpdateModel.objects.filter(id=id)
        if queryset.count() == 1:
            return queryset.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Not allowed, please use the /api/updates/ endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        # print(dir(request))
        print(request.body)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Please send using JSON."})
            return self.render_to_response(error_data, status=400)

        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = json.dumps({"message": "Something"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = json.dumps({"message": "Something"})
        return self.render_to_response(json_data, status=403)
