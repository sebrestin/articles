from django.db import models


class Sample1(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def _do_insert(self, manager, using, fields, update_pk, raw):
        return manager._insert([self], fields=fields, return_id=False,
                               using=using, raw=raw)
