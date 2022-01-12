from django.urls import include, path
from recipes.views import IngredientViewSet, RecipesViewSet, TagsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tags', TagsViewSet, basename='tags')
router.register('recipes', RecipesViewSet, basename='recipes')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
