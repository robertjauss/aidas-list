from .api_views import TaskViewSet, LoginAPIView, LogoutAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view())
]
