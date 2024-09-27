from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    #path('sign_up_tutor/', TutorCreateView.as_view(), name='tutor-create'),
    #path('all_users/', AllUsers.as_view(), name='all-users'),
    #path('all_default_users/', AllDefaultUsers.as_view(), name='all-default-users'),
    #path('all_tutors/', AllTutors.as_view(), name='all-tutors'),

    path('sign_up_user/', views.UserRegister.as_view(), name='user-create'),
    path('sign_in_user/',views.UserLogin.as_view(), name='user-login'),
    path('logout/user/', views.UserLogout.as_view(), name='logout'),
    path('current/user/', views.UserView.as_view(), name='user'),
]
