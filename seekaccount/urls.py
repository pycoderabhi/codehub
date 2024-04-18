from django.urls import path
from seekaccount import views
urlpatterns = [
    path('',views.ska,name='seekaccount')
]
