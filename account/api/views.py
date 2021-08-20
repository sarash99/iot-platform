from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from  account.models import Account
from account.api.serializers import AccountRegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate,login

@api_view(['POST',])
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        serializer = AccountRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((AllowAny,))
def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(email=email, password=password)
    data = {}
    if user:
        login(request, user)
        token , _= Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return Response(data, status=status.HTTP_200_OK)
    else:
        data['response'] = 'incorrect password or email'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
