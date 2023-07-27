from django.http import HttpRequest, JsonResponse
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest):
        return JsonResponse({})
