
from django.urls import path, include

from . import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("patex-viewset", api_views.PatexViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('batch_view/', api_views.BatchView.as_view()),
]
