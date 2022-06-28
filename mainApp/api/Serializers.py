from dataclasses import field
from pyexpat import model
from attr import fields
from rest_framework import serializers
from mainApp.models import (
                                MainCategory,
                                Course,
                                User,
                                Student,
                                Tutor,
                                PrivateTutor,
                                ContractedTutor,
                                UnavailableSlot,
                                Transaction,

)



class MainCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = MainCategory 
        fields = '__all__'


class CourseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    
class UserSerializer (serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'})
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TutorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class PrivateTutorSerializer (serializers.ModelSerializer):
    class Meta:
        model = PrivateTutor
        fields = '__all__'

class ContractedTutorSerializer (serializers.ModelSerializer):
    class Meta:
        model = ContractedTutor
        fields = '__all__'


class UnavailableSlotSerializer (serializers.ModelSerializer):
    class Meta:
        model = UnavailableSlot
        fields = '__all__'


class TransactionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'