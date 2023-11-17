# from django.db import models
# from django.conf import settings


# USER_MODEL = settings.AUTH_USER_MODEL


# class Recipe(models.Model):
#     title = models.CharField(max_length=200)
#     picture = models.URLField()
#     description = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(
#         USER_MODEL,
#         related_name="recipes",
#         on_delete=models.CASCADE,
#         null=True,
#     )
