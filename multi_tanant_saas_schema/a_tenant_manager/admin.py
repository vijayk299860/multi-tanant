from django.contrib import admin
from a_tenant_manager.models import *
# Register your models here.
class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Tenant)
        self.register(Domain)
        
tenant_admin_site = TenantAdminSite(name='Tenanat Admin Site')