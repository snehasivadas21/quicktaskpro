from django.urls import path
from .views import RegisterView,OrganizationViewSet,ProjectViewSet,TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'organization',OrganizationViewSet,basename='organization')
router.register(r'projects',ProjectViewSet,basename='projects')
router.register(r'tasks',TaskViewSet,basename='tasks')

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),

    path('token/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),

] + router.urls