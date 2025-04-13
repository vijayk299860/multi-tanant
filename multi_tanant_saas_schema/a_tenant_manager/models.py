from django.db import models
from django_tenants.models import TenantMixin,DomainMixin
# Create your models here.

class Tenant(TenantMixin):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    
class Domain(DomainMixin):
    pass
    
