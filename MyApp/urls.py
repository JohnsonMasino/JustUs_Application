import ...
from django.urls import path, include
from . import views

app_name = "MyApp"

urlpatterns = [
    path("transaction/", payment_view.as_view(), name="transaction_create"),
    path('myapp/', include('MyApp.urls')),
    path('auth/google/', views.google_auth, name='google_auth'),
    path('auth/google/callback/', views.google_auth_callback, name='google_auth_callback'),
    path("", include("allauth.urls")),
    path("authenticate/", views.my_view, name="my_view"),
]
