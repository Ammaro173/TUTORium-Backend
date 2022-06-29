from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , CreateAPIView 
from rest_framework import generics , status
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .permission import IsOwnerOrReadOnly , permissions
# for sign up
# from rest_framework import viewsets
from django.contrib.auth.models import User
from .Serializers import (
                          MyTokenObtainPairSerializer,
                          SignupSerializer
)
from rest_framework_simplejwt.views import (
                         TokenObtainPairView
)
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
from .Serializers import (
                            MainCategorySerializer,
                            CourseSerializer,
                            VisitorSerializer,
                            StudentSerializer,
                            TutorSerializer,
                            PrivateTutorSerializer,
                            ContractedTutorSerializer,
                            UnavailableSlotSerializer,
                            TransactionSerializer,
                            SignupSerializer,
                            ) 

# Catergor for cards -> list view
# when teacher post a class should choose from caterorie

from django.contrib.auth import get_user_model

# or IsAuthenticatedOrReadOnly










class MainCategorylist(ListCreateAPIView):
     queryset = MainCategory.objects.all()
     serializer_class = MainCategorySerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class MainCategoryRUD(RetrieveUpdateDestroyAPIView):
     queryset = MainCategory.objects.all()
     serializer_class = MainCategorySerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# classes 
class Courselist(ListCreateAPIView):
     queryset =  Course.objects.all()
     serializer_class =CourseSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class CourseRUD(RetrieveUpdateDestroyAPIView):
     queryset =  Course.objects.all()
     serializer_class = CourseSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class CourseCreate(CreateAPIView):
     queryset =  Course.objects.all()
     serializer_class = CourseSerializer
     


# # Visitor
# class Visitorlist(ListCreateAPIView):
#      queryset = Visitor.objects.all()
#      serializer_class =VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# class VisitorRUD(RetrieveUpdateDestroyAPIView):
#      queryset =  Visitor.objects.all()
#      serializer_class = VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

# class VisitorCreate(CreateAPIView):
#      queryset =  Visitor.objects.all()
#      serializer_class = VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# Student 
class Studentlist(ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class =StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class StudentRUD(RetrieveUpdateDestroyAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class StudentCreate(CreateAPIView):
     queryset =  Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# tutor
class Tutorlist(ListCreateAPIView):
     queryset = Tutor.objects.all()
     serializer_class =TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class TutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = Tutor.objects.all()
     serializer_class = TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class TutorCreate(CreateAPIView):
     queryset =  Tutor.objects.all()
     serializer_class = TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# PrivateTutor
class PrivateTutorlist(ListCreateAPIView):
     queryset = PrivateTutor.objects.all()
     serializer_class =PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class PrivateTutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = PrivateTutor.objects.all()
     serializer_class = PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class PrivateTutorCreate(CreateAPIView):
     queryset =  PrivateTutor.objects.all()
     serializer_class = PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# ContractedTutor
class ContractedTutorlist(ListCreateAPIView):
     queryset = ContractedTutor.objects.all()
     serializer_class =ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class ContractedTutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = ContractedTutor.objects.all()
     serializer_class = ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class ContractedTutorCreate(CreateAPIView):
     queryset =  ContractedTutor.objects.all()
     serializer_class = ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# UnavailableSlot
class UnavailableSlotlist(ListCreateAPIView):
     queryset = UnavailableSlot.objects.all()
     serializer_class =UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class UnavailableSlotRUD(RetrieveUpdateDestroyAPIView):
     queryset = UnavailableSlot.objects.all()
     serializer_class = UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class UnavailableSlotCreate(CreateAPIView):
     queryset =  UnavailableSlot.objects.all()
     serializer_class = UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# Transaction
class Transactionlist(ListCreateAPIView):
     queryset = Transaction.objects.all()
     serializer_class =TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class TransactionRUD(RetrieveUpdateDestroyAPIView):
     queryset = Transaction.objects.all()
     serializer_class = TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class TransactionCreate(CreateAPIView):
     queryset =  Transaction.objects.all()
     serializer_class = TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# sign up
# class UserViewset(viewsets.ModelViewSet):
#      queryset = User.objects.all()
#      serializer_class = SignupSerializer


# Token , Register
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


@api_view(['GET'])
def getRoutes(request):
     routes = [
          '/api/token/',
          '/api/register/',
          '/api/token/refresh/'
     ]
     return Response(routes)


# Creating private endpoint
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


