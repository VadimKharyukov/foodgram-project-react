from django.urls import include, path
from users.views import FollowListViewSet, FollowViewSet

urlpatterns = [
    path('users/<int:id>/subscribe/', FollowViewSet.as_view(),
         name='subscribe'),
    path('users/subscriptions/', FollowListViewSet.as_view(),
         name='subscription'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]
