from rest_framework.serializers import ModelSerializer
from .models import SignupCourses

class CourseSerializer(ModelSerializer):
    
    class Meta:
        model = SignupCourses
        fields = ['id', 'name', 'email', 'course']