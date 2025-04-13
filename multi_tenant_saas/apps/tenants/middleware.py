from django.http import HttpResponse
from apps.tenants.models import Tenant
from apps.tenants.router import set_current_tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get hostname from request
        hostname = request.get_host().split(':')[0]
        
        # Check for X-Tenant header (for API requests)
        tenant_id = request.headers.get('X-Tenant-Id')
        
        # Check if this is an API request that requires tenant context
        is_tenant_api = request.path.startswith('/api/v1/')
        
        # Special case for admin URLs - bypass tenant routing
        if request.path.startswith('/admin/'):
            # For admin access, don't set a tenant
            set_current_tenant(None)
            return self.get_response(request)
            
        # If not a tenant API request, don't require a tenant
        if not is_tenant_api:
            set_current_tenant(None)
            return self.get_response(request)
        
        # For tenant API requests, require a valid tenant
        try:
            if tenant_id:
                # If tenant ID is provided in header, use that
                tenant = Tenant.objects.get(id=tenant_id)
            else:
                # Otherwise, try to find tenant by domain
                tenant = Tenant.objects.get(domain=hostname)
                
            # Set the tenant in the request and thread local
            request.tenant = tenant
            set_current_tenant(tenant)
            
        except Tenant.DoesNotExist:
            # If no tenant is found for an API request, return an error
            return HttpResponse("Tenant not found", status=404)
        
        response = self.get_response(request)
        return response
