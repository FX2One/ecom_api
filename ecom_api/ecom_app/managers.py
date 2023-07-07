from django.db import models
from django.db.models import Q


class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)



