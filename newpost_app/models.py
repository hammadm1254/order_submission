from django.db import models
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200, blank=False)
    weight = models.DecimalField(max_digits= 6, decimal_places=2, blank=False)
    length = models.DecimalField(max_digits= 6, decimal_places=2, blank=False)
    width = models.DecimalField(max_digits= 6, decimal_places=2, blank=False)
    height = models.DecimalField(max_digits= 6, decimal_places=2, blank=False)
    special_instructions = models.TextField(max_length=1000, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    submitted_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.submitted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title