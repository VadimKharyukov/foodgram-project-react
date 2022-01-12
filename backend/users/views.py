from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from recipes.permissions import IsAuthorOrReadOnly
from users.serializers import FollowSerializers, FollowListSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import Follow, CustomUser
from recipes.pagination import CustomPaginator


class FollowListViewSet(ListAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = CustomPaginator

    def get(self, request):
        user = request.user
        queryset = CustomUser.objects.filter(following__user=user)
        page = self.paginate_queryset(queryset)
        serializer = FollowListSerializers(page, many=True)
        return self.get_paginated_response(serializer.data)


class FollowViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, id):
        data = {'user': request.user.id,
                'author': id}
        serializer = FollowSerializers(data=data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        author = get_object_or_404(CustomUser, id=id)
        follow = get_object_or_404(Follow, user=user, author=author)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
