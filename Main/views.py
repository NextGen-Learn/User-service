from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import UserDefault, Tutor
from .serializers import *
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateView(generics.CreateAPIView):
    queryset = UserDefault.objects.all()
    serializer_class = UserDefaultSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class TutorCreateView(generics.CreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tutor = serializer.save()
        refresh = RefreshToken.for_user(tutor)

        return Response({
            'tutor': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class AllDefaultUsers(APIView):
    def get(self, request):
        user_defaults = UserDefault.objects.all()
        user_default_serializer = UserDefaultSerializer(user_defaults, many=True)

        return Response({
            'user_defaults': user_default_serializer.data,
        })

class AllTutors(APIView):
    def get(self, request):
        tutors = Tutor.objects.all()
        tutor_serializer = TutorSerializer(tutors, many=True)

        return Response({
            'tutors': tutor_serializer.data,
        })
    
class AllUsers(APIView):
     def get(self, request):
        user_defaults = UserDefault.objects.all()
        tutors = Tutor.objects.all()

        user_default_serializer = UserDefaultSerializer(user_defaults, many=True)
        tutor_serializer = TutorSerializer(tutors, many=True)

        return Response({
            'user_defaults': user_default_serializer.data,
            'tutors': tutor_serializer.data
        })

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.last_login = timezone.now()
            user.save()

            return Response({
                'message': 'Login successful',

                'user': {
                    'id': user.id,
                    'email': user.email,
                    'user_name': user.user_name,
                    'avatar': user.avatar,
                    'last_login': user.last_login
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)