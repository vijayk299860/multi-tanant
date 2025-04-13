from django.http import HttpResponseNotFound
from django_tenants.utils import get_public_schema_name

class PublicAdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin_tenants/'):
            # Make sure the request has a tenant attached
            if hasattr(request, 'tenant'):
                # If this is NOT the public tenant (i.e., a real tenant schema)
                if request.tenant.schema_name != get_public_schema_name():
                    return HttpResponseNotFound("Not allowed to See Tenant admin panel")
        return self.get_response(request)
