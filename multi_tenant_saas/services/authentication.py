from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from apps.tenants.router import get_current_tenant

class TenantAwareTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Get current tenant
        tenant = get_current_tenant()
        if not tenant:
            raise serializers.ValidationError("No tenant context found")
        
        # Authenticate against the tenant's database
        username = attrs.get('username')
        password = attrs.get('password')
        
        # Django's authenticate doesn't support explicit database selection
        # So we need to manually check the user
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError("Invalid credentials")
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")
        
        # Create token payload
        refresh = self.get_token(user)
        
        # Add tenant information to the token
        refresh['tenant_id'] = tenant.id
        refresh['tenant_name'] = tenant.name
        refresh['db_name'] = tenant.db_name
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class TenantAwareTokenObtainPairView(TokenObtainPairView):
    serializer_class = TenantAwareTokenObtainPairSerializer
