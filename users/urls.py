from django.urls import re_path

from users.views import LoginView, LogoutView, SignupView, AddBalanceView, PurchaseListView, PurchaseDeleteView

app_name = 'users'

urlpatterns = [
    re_path('login', LoginView.as_view()),
    re_path('logout', LogoutView.as_view()),
    re_path('signup', SignupView.as_view()),
    re_path('add_balance', AddBalanceView.as_view()),
    re_path('purchases', PurchaseListView.as_view()),
    re_path(r'delete_purchase/(?P<id>[0-9]+)/$', PurchaseDeleteView.as_view()),
]