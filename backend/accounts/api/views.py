from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from drf_spectacular.utils import extend_schema
from ..models import CustomUser
from .serializers import UserSerializer, LoginSerializer


@extend_schema(tags=["Authentication"])
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        request.data["user_type"] = "client"
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = authenticate(
            request, email=request.data["email"], password=request.data["password"]
        )
        login(request, user)

        return Response(
            {"user_id": user.id},
            headers=headers,
        )


@extend_schema(tags=["Authentication"])
class UserLoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return Response({"user_id": user.id})
        else:
            return Response({"error": "Invalid credentials"}, status=400)
