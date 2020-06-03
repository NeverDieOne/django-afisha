from django.urls import path
from .views import index, place_detail


urlpatterns = [
    path('', index, name='main_page'),
    path('place/<pk>', place_detail, name='place_detail')
]
