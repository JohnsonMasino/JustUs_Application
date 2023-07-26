from MyApp.views import payment_view
from django.urls import path

app_name = "MyApp"

urlpatterns = [
    path("transaction/", payment_view.as_view(), name="transaction_create"),
    path('myapp/', include('MyApp.urls'))
]