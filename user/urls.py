from django.urls import path

from user.views import TeacherRegistrationView, StudentRegistrationView, VisitorRegistrationView, \
    CustomTokenObtainPairView, UserProfileView

urlpatterns = [
    path('api/teacher/register/', TeacherRegistrationView.as_view(), name='teacher-register'),
    path('api/student/register/', StudentRegistrationView.as_view(), name='student-register'),
    path('api/visitor/register/', VisitorRegistrationView.as_view(), name='visitor-register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]