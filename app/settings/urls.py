
from django.contrib import admin
from django.urls import path
from currency.views import generate_password
from currency.views import rate_list
from currency.views import rate_details
from currency.views import source_list
from currency.views import source_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen-pass/', generate_password),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/source/details/<int:pk>/', source_details),
    path('currency/source/list/', source_list),

]
