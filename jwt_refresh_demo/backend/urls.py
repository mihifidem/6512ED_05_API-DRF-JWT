from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView, MeView

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Cuentas
    path("api/register/", RegisterView.as_view()),
    path("api/me/", MeView.as_view()),
]
