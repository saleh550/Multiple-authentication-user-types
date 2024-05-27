from rest_framework import serializers
from .models import CustomUser, Teacher, Student, Visitor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ('user', 'subject')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


class StudentRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'average')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student


class VisitorRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Visitor
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        visitor = Visitor.objects.create(user=user, **validated_data)
        return visitor


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        if hasattr(self.user, 'teacher'):
            data['subject'] = self.user.teacher.subject
        elif hasattr(self.user, 'student'):
            data['average'] = self.user.student.average
        # You can add more fields for visitor or other roles if needed
        return data


# getprofile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Teacher
        fields = ('user', 'subject')


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Student
        fields = ('user', 'average')


class VisitorProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Visitor
        fields = ('user',)
