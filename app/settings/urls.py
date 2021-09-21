from django.contrib import admin
from django.urls import path
from currency.views import (
    generate_password,
    rate_list, rate_details,
    rate_create, rate_update, rate_delete,
    source_list, source_details, source_create,
    source_update, source_delete, index,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gen-pass/', generate_password),

    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/rate/create/', rate_create),
    path('currency/rate/update/<int:pk>/', rate_update),
    path('currency/rate/delete/<int:pk>/', rate_delete),

    path('currency/source/list/', source_list),
    path('currency/source/details/<int:pk>/', source_details),
    path('currency/source/create/', source_create),
    path('currency/source/update/<int:pk>/', source_update),
    path('currency/source/delete/<int:pk>/', source_delete),

]
