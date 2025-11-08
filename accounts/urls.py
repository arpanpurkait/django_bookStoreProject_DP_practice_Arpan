# accounts/urls.py
from django.urls import path
from .views import SignUpPageView  # ✅ yaha sahi class name likho

urlpatterns = [
    path("signup/", SignUpPageView.as_view(), name="signup"),  # ✅ correct reference
]
