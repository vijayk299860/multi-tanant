from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    db_name = models.CharField(max_length=63, unique=True)
    domain = models.CharField(max_length=253, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.name} ({self.domain})"
