from django.urls import path

from accounts.views import SignUpCreateView

app_name = 'my-account'

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='sign-up'),
]
