from django.urls import path
from .views import Loginview,SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',Loginview.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/', SignUpView.as_view(), name='signup'),
]