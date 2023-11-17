from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "vegetarian",
        "vegan",
        "created_on",
        "updated_on",
    ]

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "step_number",
        "instruction",
        "id",
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "amount",
        "food_item",
    )
