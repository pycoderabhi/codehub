from django.urls import path
from upaccount import views
urlpatterns = [
    path('',views.upa,name='upaccount')
]
