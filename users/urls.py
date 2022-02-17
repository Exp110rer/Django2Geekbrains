from django.urls import path, re_path

from users.views import UserLoginView, UserLogoutView, register, UserProfileView, verify
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    re_path(r'verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify')
]
