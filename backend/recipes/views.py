from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.filters import IngredientSearchFilter, RecipeFilter
from recipes.models import (Favorite, Ingredient, Purchase, Recipe,
                            RecipeIngredient, Tag)
from recipes.pagination import CustomPaginator
from recipes.permissions import IsAuthorOrReadOnly
from recipes.serializers import (FavoriteSerializers, IngredientSerializers,
                                 PurchaseSerializers, RecipeListSerializers,
                                 RecipeSerializers, TagSerializers)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class TagsViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = (AllowAny, )


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
    permission_classes = (AllowAny, )
    filter_backends = (IngredientSearchFilter, )
    search_fields = ('^name', )


class RecipesViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RecipeFilter
    pagination_class = CustomPaginator

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializers
        return RecipeSerializers

    @staticmethod
    def post_method(request, pk, serializers):
        data = {'user': request.user.id,
                'recipe': pk}
        serializer = serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        return self.post_method(request=request, pk=pk,
                                serializers=FavoriteSerializers)

    @staticmethod
    def delete_method(request, pk, model):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        model_obj = get_object_or_404(model, user=user, recipe=recipe)
        model_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        return self.delete_method(request=request, pk=pk, model=Favorite)

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk):
        return self.post_method(request=request, pk=pk,
                                serializers=PurchaseSerializers)

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk):
        return self.delete_method(request=request, pk=pk, model=Purchase)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = RecipeIngredient.objects.filter(
            recipe__purchases__user=request.user).values(
            'ingredient__name',
            'ingredient__measurement_unit').annotate(total=Sum('amount'))
        shopping_list = 'список:\n'
        for number, ingredient in enumerate(ingredients, start=1):

            shopping_list += (
                f'{number} '
                f'{ingredient["ingredient__name"]} - '
                f'{ingredient["total"]} '
                f'{ingredient["ingredient__measurement_unit"]}\n')

        purchase_list = 'purchase_list.txt'
        response = HttpResponse(shopping_list, content_type='text/plain')
        response['Content-Disposition'] = (f'attachment;'
                                           f'filename={purchase_list}')
        return response
