from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from  account.models import Account
from account.api.serializers import AccountRegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

@api_view(['POST',])
@permission_classes((AllowAny,))
@csrf_exempt
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
@csrf_exempt
def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(email=email, password=password)
    data = {}
    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return Response(data, status=status.HTTP_200_OK)
    else:
        data['response'] = 'incorrect password or email'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def detail_view(request):
    account = request.user
    data = {}
    if account:
        data['username'] = account.username
        return Response(data, status=status.HTTP_200_OK)
    else:
        data['response'] = 'this account does not exist'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)