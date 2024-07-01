from django.db import models
from typing import Optional

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='direct_reports')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
