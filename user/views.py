from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher, Student, Visitor, CustomUser
from .serializers import TeacherRegistrationSerializer, StudentRegistrationSerializer, VisitorRegistrationSerializer, \
    TeacherProfileSerializer, StudentProfileSerializer, VisitorProfileSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class TeacherRegistrationView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherRegistrationSerializer
    permission_classes = [AllowAny]


class StudentRegistrationView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegistrationSerializer
    permission_classes = [AllowAny]


class VisitorRegistrationView(generics.CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorRegistrationSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.role == CustomUser.TEACHER:
            profile = Teacher.objects.get(user=user)
            serializer = TeacherProfileSerializer(profile)
        elif user.role == CustomUser.STUDENT:
            profile = Student.objects.get(user=user)
            serializer = StudentProfileSerializer(profile)
        elif user.role == CustomUser.VISITOR:
            profile = Visitor.objects.get(user=user)
            serializer = VisitorProfileSerializer(profile)
        else:
            serializer = UserProfileSerializer(user)

        return Response(serializer.data)