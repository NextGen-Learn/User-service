# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
# from .models import UserDefault, Tutor
# from .serializers import *
# from django.utils import timezone
# from rest_framework_simplejwt.tokens import RefreshToken
from venv import logger
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer,UserSerializer
from rest_framework import permissions, status
from django.core.exceptions import ValidationError

from .validations import custom_validation, validate_email, validate_password


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)

        if serializer.is_valid(raise_exception=True) :
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class TutorCreateView(generics.CreateAPIView):
#     queryset = Tutor.objects.all()
#     serializer_class = TutorSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         tutor = serializer.save()
#         refresh = RefreshToken.for_user(tutor)

#         return Response({
#             'tutor': serializer.data,
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_201_CREATED)

# class AllDefaultUsers(APIView):
#     def get(self, request):
#         user_defaults = UserDefault.objects.all()
#         user_default_serializer = UserDefaultSerializer(user_defaults, many=True)

#         return Response({
#             'user_defaults': user_default_serializer.data,
#         })

# class AllTutors(APIView):
#     def get(self, request):
#         tutors = Tutor.objects.all()
#         tutor_serializer = TutorSerializer(tutors, many=True)

#         return Response({
#             'tutors': tutor_serializer.data,
#         })
    
# class AllUsers(APIView):
#      def get(self, request):
#         user_defaults = UserDefault.objects.all()
#         tutors = Tutor.objects.all()

#         user_default_serializer = UserDefaultSerializer(user_defaults, many=True)
#         tutor_serializer = TutorSerializer(tutors, many=True)

#         return Response({
#             'user_defaults': user_default_serializer.data,
#             'tutors': tutor_serializer.data
#         })

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user) 
            return Response({"message": "Login successful!", "user": user.username}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogout(APIView):
    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        else:
            logger.debug(f'User not authenticated: {request.user}')
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)