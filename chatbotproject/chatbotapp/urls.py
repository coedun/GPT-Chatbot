from django.urls import path
from .views import execute_model

urlpatterns = [
    path("execute-model/", execute_model, name="execute_model"),
]