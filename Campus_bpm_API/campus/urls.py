from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campus.api.views import MusicaViewSet, BpmViewSet

router = DefaultRouter()
router.register(r'musicas', MusicaViewSet)
router.register(r'registro', BpmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]