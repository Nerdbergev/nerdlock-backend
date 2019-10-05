from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('api-token-auth', views.obtain_auth_token),
    path('', include('door.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
