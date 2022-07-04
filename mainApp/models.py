from django.db import models
from django.contrib.auth import get_user_model
from polymorphic.models import PolymorphicModel

# from django.contrib.contenttypes.models import ContentType

# Create your models here.

# category model
class MainCategory(models.Model):
    name = models.CharField(max_length=100)  # {_id :1,name: programming}

    def __str__(self):
        return self.name


# University model
# class University(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# wallet system model

# i change user to visitor
class Visitor(models.Model):

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # model.password? check forms?
    contact = models.CharField(max_length=20, blank=True)
    country = models.TextField(max_length=255, null=True)
    city = models.TextField(max_length=255, null=True)
    Education = models.TextField(max_length=255, null=True)
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    # wallet = models.OneToOneField(Wallet)

    # def create_wallet(self):
    #     wallet = Wallet(balance=0)
    #     wallet.save()

    #     # self.wallet = wallet
    #     return wallet
    def __str__(self):
        return self.name

    # def be_student(self):
    #     student = Student(user=self)
    #     student.save()
    #     return student

    def be_tutor(self, short_bio, is_private, rate=0):
        if is_private:
            tutor = PrivateTutor(user=self, shortBio=short_bio, rate=rate)
            tutor.save()
        else:
            tutor = ContractedTutor(user=self, shortBio=short_bio)
            tutor.save()
        return tutor

    def get_upcoming_bookings(self, isTutor, isStudent):
        statusToGEt = ["BOOKED", ""]


# Student Models
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField("Course")

    def _get_courses_student(self):
        return "/\t".join([ele.name for ele in self.courses.all()])

    # forign keys
    # gender = models.BooleanField()
    # image

    def __str__(self):
        return self.name


# Tutor Model
class Tutor(PolymorphicModel):
    name = models.CharField(max_length=255, help_text="Enter a Name")
    age = models.PositiveIntegerField(help_text="Enter an Age")
    teaching_experience = models.PositiveIntegerField(
        help_text="Enter the teaching Experience period"
    )
    # comment the 2 line bellow
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    courses_in = models.ManyToManyField(
        "Course", related_name="+"
    )  # check many to many or foreign key
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
    # gender = models.BooleanField()
    # image

    def __str__(self):
        return self.name

    # function for list_display in admin.py
    def _get_courses(self):
        return "/\t".join([ele.name for ele in self.courses.all()])


# viewed courses model
class Course(models.Model):
    name = models.CharField(max_length=255)
    # is_available_private = models.BooleanField(default=True)
    course_category = models.ForeignKey(
        MainCategory, on_delete=models.CASCADE
    )  # {_id:1 , course_name : py , course_category : programming}
    price = models.IntegerField(default=0, null=True)
    short_bio = models.TextField(default="", null=True)
    description = models.TextField(max_length=1000, null=True)
    available_seat = models.PositiveIntegerField(default=1, null=True)
    zoom_link = models.URLField(max_length=200, null=True)
    likes = models.PositiveIntegerField(default=0, null=True)
    tutors = models.ForeignKey(
        "Tutor", on_delete=models.CASCADE, null=True, default=None, related_name="+"
    )
    students_in = models.ManyToManyField(Student, related_name="+")
    schedule = models.TimeField(null=True)

    def __str__(self):
        return self.name


class PrivateTutor(Tutor):

    rate = models.PositiveIntegerField()

    def __str__(self):
        return self.user.name

    def create_unavailable_slot(self, date, time_start):
        unavailable = UnavailableSlot(
            tutor=self, date=date, time_start=time_start, duration=1.0
        )
        unavailable.save()


class ContractedTutor(Tutor):
    def __str__(self):
        return self.user.name

    def create_unavailable_slot(self, date, time_start):
        unavailable = UnavailableSlot(
            tutor=self, date=date, time_start=time_start, duration=0.5
        )
        unavailable.save()


class UnavailableSlot(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # day = models.CharField(max_length=3)
    date = models.DateField()
    time_start = models.TimeField()
    duration = models.FloatField()


class Transaction(PolymorphicModel):
    user = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField()


# class CourseDetails(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     course_category = models.ForeignKey(
#         MainCategory, on_delete=models.CASCADE, default=1
#     )
#     price


# class Wallet(PolymorphicModel):
#     balance = models.FloatField()

#     def add_funds(
#         self,
#         amount,
#     ):
#         self.balance += amount


######################

# class Table(models.Model):
#     seats = models.IntegerField()
#     min_people = models.IntegerField()
#     max_people = models.IntegerField()


# class Reservation(models.Model):
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#     party = models.ForeignKey(User, on_delete=models.CASCADE)
#     spot = (
#         models.DateField()
#     )  # Make sure you don't use 'time' for this field, as that will cause a headache later on.
