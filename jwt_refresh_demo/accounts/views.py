from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers

# --- Registro de usuario ---
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# --- Perfil protegido ---
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class MeView(generics.RetrieveAPIView):
    serializer_class = MeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
