"""
URL configuration for EduExam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('get_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    path('part1/', Part1Api.as_view()),
    path('part2/', Part2Api.as_view()),
    path('part3/', Part3Api.as_view()),
    path('settings/', Settings.as_view()),
    path('status/', CheckSubscription.as_view()),
    path('audio/', AudioApi.as_view()),
    path('user/', TestTakerApi.as_view()),
    path('download/<slug:pk>/', FileDownloadView.as_view()),
    path('clean/<slug:pk>/', CleanTrash.as_view()),
    path('shart/', ShartAudio.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

