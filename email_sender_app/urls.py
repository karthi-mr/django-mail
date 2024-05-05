from typing import Any

from django.urls import path

from email_sender_app import views

urlpatterns: list[Any] = [
    path('send-mail', views.index), # type: ignore
]