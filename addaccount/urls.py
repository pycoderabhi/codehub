from django.urls import path
from addaccount import views
urlpatterns = [
    path('',views.adc, name='addaccount')
]
