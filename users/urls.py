from django.urls import re_path

from users.views import LoginView, LogoutView, SignupView

app_name = 'users'

urlpatterns = [
    re_path('login', LoginView.as_view()),
    re_path('logout', LogoutView.as_view()),
    re_path('signup', SignupView.as_view()),
]