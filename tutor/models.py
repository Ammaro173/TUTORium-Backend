from django.db import models
from django.contrib.auth import get_user_model
from polymorphic.models import PolymorphicModel

# Create your models here.

# category model
class MainCategory(models.Model):
    name = models.CharField(max_length=100)  # {_id :1,name: programming}

    def __str__(self):
        return self.name


# University model
class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# viewed courses model
class Course(models.Model):
    name = models.CharField(max_length=255)
    course_category = models.ForeignKey(
        MainCategory, on_delete=models.CASCADE
    )  # {_id:1 , course_name : py , course_category : programming}

    def __str__(self):
        return self.name


# wallet system model
class Wallet(PolymorphicModel):
    balance = models.FloatField()

    def add_funds(
        self,
        amount,
    ):
        self.balance += amount


class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # model.password? check forms?
    contact = models.CharField(max_length=20, blank=True)
    wallet = models.OneToOneField(Wallet)

    def create_wallet(self):
        wallet = Wallet(balance=0)
        wallet.save()  # This performs an INSERT SQL statement behind the scenes. Django doesn’t hit the database until you explicitly call save(). The save() method has no return value.

        # self.wallet = wallet
        return wallet

    def be_student(self):
        student = Student(user=self)
        student.save()
        return student

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
    courses = models.ManyToManyField(Course)
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

    # under sh3`l`  one to one !
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)  # check many to many or foreign key
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
    # gender = models.BooleanField()
    # image

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
    user = models.ForeignKey(User)
    amount = models.FloatField()
    date = models.DateField()
    time = models.TimeField()


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


## dont foregt to mack branches
## how to add multiple categories ?? (multiple foreign key for the same key)
## how to make sure subCategory is only connected to its Main categorty !!
## k3ksh in django function inside classes ()
### check user settings before creating super use thing!!
## add wallet system   polymorphic>?
