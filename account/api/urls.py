from django.conf.urls import url
from account.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    url(r'^register/', views.registration_view, name="register"),
    url(r'^login/', views.login_view, name="login"),
    url(r'^detail/', views.detail_view, name="detail")
]