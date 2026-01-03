"""

    URL mappings for the recipe API

"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter  # noqa

from recipe import views  # noqa

router = DefaultRouter()
router.register('recipe', views.RecipeViewSet)
router.register('tag', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]



