from django.urls import path
from delaccount import views
urlpatterns = [
    path('',views.dla,name='dla'),
    path('dlac',views.dlac,name='dlac')
]
