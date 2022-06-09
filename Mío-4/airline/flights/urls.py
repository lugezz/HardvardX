from django.urls import path, include

from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.home_view, name="flights"),
    path('<int:fl_id>/', views.flight_view, name= 'flight_view'),
    path('<int:fl_id>/book', views.flight_book, name= 'flight_book'),
]
