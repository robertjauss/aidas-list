from .views import HomeView, LoginView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view()),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
