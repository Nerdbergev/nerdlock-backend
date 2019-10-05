from django.urls import path

from door import views

urlpatterns = [
    path('open', views.open),
    path('close', views.close),
    path('status', views.DoorStatusDetail.as_view())
]
