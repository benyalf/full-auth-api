from django.urls import path, re_path
from .views import (
    customProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    # URL Para hacer llamado a facebook o google
    re_path(
        r'^o/(?P<provider>\S+)/$',
        customProviderAuthView.as_view(),
        name='provider-auth'
    ),


    # Url Views Custom JWT Authentication
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),


]
