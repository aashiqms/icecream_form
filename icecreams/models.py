from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IceCream(models.Model):
    flavour1 = models.CharField(max_length=100)
    flavour2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


