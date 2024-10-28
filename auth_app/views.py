from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from django.contrib.auth import aauthenticate

# Create your views here.



@api_view(['GET'])
def test_api(request):
    return Response({"message": "Hello, the API is working!"})


@api_view(['POST'])
def register_view(request):
    serilizer = RegisterSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response({"message": "User created succefully"}, status=status.HTTP_201_CREATED)
    return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def custom_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = aauthenticate(username=username, password=password)


    if user is not None:

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

    return Response({'detail': 'Invalid credentials'},  status=status.HTTP_401_UNAUTHORIZED)