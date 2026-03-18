from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer
from .models import User
from .permissions import HasRolePermission
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "user": serializer.data,
                "message": "Аккаунт успешно создан!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Вы успешно вышли"}, status=205)
        except Exception:
            return Response({"error": "Неверный токен или поле 'refresh' отсутствует"}, status=400)


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class AdminOnlyDataView(generics.GenericAPIView):
    permission_classes = [HasRolePermission]
    required_roles = ['admin']

    def get(self, request):
        return Response({
            "message": "Доступ разрешен: У вас есть роль АДМИНА",
            "secret_objects": ["Объект А", "Объект Б"]
        })

class ClientDataView(generics.GenericAPIView):
    permission_classes = [HasRolePermission]
    required_roles = ['admin', 'client']

    def get(self, request):
        return Response({
            "message": "Доступ разрешен: Вы Админ или Клиент",
            "public_objects": ["Товар 1", "Товар 2"]
        })