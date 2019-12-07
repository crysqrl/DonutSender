from django.db import models


class Singleton(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(Singleton, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
