from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^register/$' , views.registration_view , name = "register"),
    url(r'^logout/$' , views.logout_view , name = "logout"),
    url(r'^login/$' , views.login_view , name="login"),
]


