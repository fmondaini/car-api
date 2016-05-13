from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'manufacturer', views.ManufacturerViewSet)
router.register(r'carmodel', views.CarModelViewSet)
router.register(r'car', views.CarViewSet)
router.register(r'service', views.ServiceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework')),

    url(r'^', include(router.urls)),
]
