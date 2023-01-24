from rest_framework import serializers
from .models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['full_name', 'email', 'password', 
                'qualification', 'mobile_no', 'address']