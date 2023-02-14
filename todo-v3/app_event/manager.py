from django.db import models


class eventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class todoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
