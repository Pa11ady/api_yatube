from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


VERSION = '1'

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path(f'v{VERSION}/', include(router.urls)),
    path(f'v{VERSION}/api-token-auth/', views.obtain_auth_token),
]
