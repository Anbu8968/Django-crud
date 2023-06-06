from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class customMiddleware(MiddlewareMixin):
    def process_request(self,request):
        api = (request.get_full_path().split('?')[0]).split('/')
        length = len(api)
        print(request.body.decode('utf-8'))
        pass
