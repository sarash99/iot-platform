from django.conf.urls import url
from account.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    url(r'^register/', views.registration_view, name="register"),
    url(r'^login/', obtain_auth_token, name="login")
]