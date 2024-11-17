from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from core.forms import UserAuthenticationForm
from users.views import SignupView, ProfileView, BalanceAddView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=UserAuthenticationForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('balance_add/', BalanceAddView.as_view(), name='balance_add'),
]