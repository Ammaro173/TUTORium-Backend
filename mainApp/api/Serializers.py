from rest_framework import serializers
from mainApp.models import (
    MainCategory,
    Course,
    Visitor,
    Student,
    Tutor,
    PrivateTutor,
    ContractedTutor,
    UnavailableSlot,
    Transaction,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# sign up
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    course_category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Course
        fields = "__all__"


class VisitorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = Visitor
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = "__all__"


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"


class PrivateTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateTutor
        fields = "__all__"


class ContractedTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractedTutor
        fields = "__all__"


class UnavailableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnavailableSlot
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


# generating token Serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token


# Sign up API
MinLength = 8


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MinLength,
        error_messages={
            "min_length": "Password must be longer than {MinLength} characters."
        },
    )

    ensure_password = serializers.CharField(
        write_only=True,
        min_length=MinLength,
        error_messages={
            "min_length": "Password must be longer than {MinLength} characters."
        },
    )

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["ensure_password"]:
            raise serializers.ValidationError("password does not match. ")

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            # active = validated_data['active']
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


# # log in
# class LoginSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = get_user_model()
#             field = '__all__'
