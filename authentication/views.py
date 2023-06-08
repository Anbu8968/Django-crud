from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password,check_password
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        name=request.data['name']
        email=request.data['email']
        password=request.data['password']
        user = User.objects.create(name=name,email=email,password=password)
        # user.password(password)
        return Response(user.password)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email,password=password).first()
        print(user)

        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.password!=password:
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').encode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            "Status":"Login Successfull"
        }
        return response




class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout success'
        }
        return response