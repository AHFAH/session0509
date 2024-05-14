from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewsets', PostModelViewSet)

app_name = 'posts'

urlpatterns = [
    path('post/', PostAPIView.as_view()),
    path('list', PostList.as_view()),
    path('comment/', CommentCreate),
]
