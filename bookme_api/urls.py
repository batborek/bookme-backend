from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from bookme_api import views


router = DefaultRouter()
router.register('register', views.UserProfileViewSet)
router.register('rooms',views.RoomsViewSet)


urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]