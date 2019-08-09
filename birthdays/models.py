from django.db import models


class Friend(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
