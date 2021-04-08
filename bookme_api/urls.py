from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from bookme_api import views

router = DefaultRouter()
router.register('rooms', views.RoomsViewSet)


urlpatterns = [
    path('',include(router.urls))
]