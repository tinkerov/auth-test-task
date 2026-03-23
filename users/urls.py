from django.urls import path
from .views import RegisterView, UserProfileView, LogoutView, AdminOnlyDataView, ClientDataView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('admin-data/', AdminOnlyDataView.as_view(), name='admin_data'),
    path('client-data/', ClientDataView.as_view(), name='client_data'),
]