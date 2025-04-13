from threading import local

_thread_local = local()

def get_current_tenant():
    return getattr(_thread_local, 'tenant', None)

def set_current_tenant(tenant):
    _thread_local.tenant = tenant

class TenantDatabaseRouter:
    """
    Database router that routes queries to tenant-specific databases.
    """
    def db_for_read(self, model, **hints):
        # Tenant model always uses default database
        if model._meta.app_label == 'tenants' and model._meta.model_name == 'tenant':
            return 'default'
            
        # Use tenant database for all other models
        tenant = get_current_tenant()
        if tenant:
            return tenant.db_name
        return 'default'

    def db_for_write(self, model, **hints):
        # Tenant model always uses default database
        if model._meta.app_label == 'tenants' and model._meta.model_name == 'tenant':
            return 'default'
            
        # Use tenant database for all other models
        tenant = get_current_tenant()
        if tenant:
            return tenant.db_name
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the same database
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Only allow tenant model migrations on default database
        if app_label == 'tenants' and model_name == 'tenant':
            return db == 'default'
            
        # Allow all other migrations on all databases
        return True
