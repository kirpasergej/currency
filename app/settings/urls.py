
from django.contrib import admin
from django.urls import path
from currency.views import generate_password
from currency.views import hello_world
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen-pass/', generate_password),
    path('hello_world/', hello_world),
]
