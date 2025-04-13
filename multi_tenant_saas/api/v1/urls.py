from django.urls import path, include
from services.authentication import TenantAwareTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authentication endpoints
    path('token/', TenantAwareTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # App endpoints
    # path('blog/', include('apps.blog.urls')),
    # path('messaging/', include('apps.messaging.urls')),
]
