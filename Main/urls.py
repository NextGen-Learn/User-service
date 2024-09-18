from django.urls import path
from .views import UserCreateView, TutorCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('sign_up_user/', UserCreateView.as_view(), name='user-create'),
    path('sign_up_tutor/', TutorCreateView.as_view(), name='tutor-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
