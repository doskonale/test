from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from test_app import views
from rest_framework.authtoken import views as auth_views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'projects', views.ProjectViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
