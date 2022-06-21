from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


# category model
class MainCategory(models.Model):
    name = models.CharField(max_length=100)  # {_id :1,name: programming}

    def __str__(self):
        return self.name


# viewed courses model
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_category = models.ForeignKey(
        MainCategory, on_delete=models.CASCADE
    )  # {_id:1 , course_name : py , course_category : programming}

    def __str__(self):
        return self.name


# Student Models
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_timestamp = models.DateTimeField(auto_now_add=True)
    student_updatedtime = models.DateTimeField(auto_now=True)
    # gender = models.BooleanField()
    # image

    def __str__(self):
        return self.name


# Tutor Model
class Tutor(models.Model):
    tutor_name = models.CharField(max_length=255, help_text="Enter a Name")
    tutor_age = models.IntegerField(help_text="Enter an Age")
    tutor_teaching_experience = models.IntegerField(
        help_text="Enter the teaching Experience period"
    )

    # under sh3`l`
    tutor_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    tutor_courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    tutor_timestamp = models.DateTimeField(auto_now_add=True)
    tutor_updatedtime = models.DateTimeField(auto_now=True)
    # gender = models.BooleanField()
    # image

    def __str__(self):
        return self.name


## dont foregt to mack branches
## how to add multiple categories ?? (multiple foreign key for the same key)
## how to make sure subCategory is only connected to its Main categorty !!
## k3ksh in django function inside classes ()
## check user settings before creating super use thing!!
