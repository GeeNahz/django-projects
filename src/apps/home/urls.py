from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.home_view, name='home'),
]
