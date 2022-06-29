from posixpath import basename
from unicodedata import name
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    
)
from . import views
from .api.views import (
                   MyTokenObtainPairView,
                   RegisterView,
                   getRoutes,
                   testEndPoint,
                  )
from django.urls import path
from mainApp.api.views import ( MainCategorylist, 
                                MainCategoryRUD,
                                Courselist,
                                CourseRUD,
                                CourseCreate,
                                # Visitorlist,
                                # VisitorRUD,
                                # VisitorCreate,
                                Studentlist,
                                StudentRUD,
                                StudentCreate, 
                                Tutorlist,
                                TutorRUD,
                                TutorCreate,
                                PrivateTutorlist,
                                PrivateTutorRUD,
                                PrivateTutorCreate,
                                ContractedTutorlist,
                                ContractedTutorRUD,
                                ContractedTutorCreate,
                                UnavailableSlotlist,
                                UnavailableSlotRUD,
                                UnavailableSlotCreate, 
                                Transactionlist,
                                TransactionRUD,
                                TransactionCreate, 
                                      )



# router = DefaultRouter()
# router.register('user' , UserViewset)


urlpatterns = [
    # Category
    path('category',MainCategorylist.as_view(), name = 'category_list'),
    path('category-rud/<int:pk>',MainCategoryRUD.as_view(), name = 'category_list_rud'),


    # course
    path('courses',Courselist.as_view(), name = 'courses_list'),
    path('courses-rud/<int:pk>',CourseRUD.as_view(), name = 'courses_list_rud'),
    path('course-post' , CourseCreate.as_view(), name='create_post'),


    # # visitor
    # path('visitor',Visitorlist.as_view(), name = 'visitor_list'),
    # path('visitor-rud/<int:pk>',VisitorRUD.as_view(), name = 'courses_list_rud'),
    # path('visitor-post' , VisitorCreate.as_view(), name='visitor_post'),


    # Student
    path('student',Studentlist.as_view(), name = 'student_list'),
    path('student-rud/<int:pk>',StudentRUD.as_view(), name = 'courses_list_rud'),
    path('student-post' , StudentCreate.as_view(), name='student_post'),


    # Tutor
    path('tutor', Tutorlist.as_view(), name = 'tutor_list'),
    path('tutor-rud/<int:pk>', TutorRUD.as_view(), name = 'tutor_list_rud'),
    path('tutor-post' ,   TutorCreate.as_view(), name='tutor_post'),


    # privateTutor
    path('privateTutor', PrivateTutorlist.as_view(), name = 'privateTutor_list'),
    path('privateTutor-rud/<int:pk>', PrivateTutorRUD.as_view(), name = 'privateTutor_list_rud'),
    path('privateTutor-post' ,   PrivateTutorCreate.as_view(), name='privateTutor_post'),


    # contractedTutor
    path('contractedTutor', ContractedTutorlist.as_view(), name = 'contractedTutor_list'),
    path('contractedTutor-rud/<int:pk>', ContractedTutorRUD.as_view(), name = 'contractedTutor_list_rud'),
    path('privateTutor-post' ,   ContractedTutorCreate.as_view(), name='contractedTutor_post'),

    # unavailableSlot
    path('unavailableslot', UnavailableSlotlist.as_view(), name = 'unavailableslot_list'),
    path('unavailableslot-rud/<int:pk>', UnavailableSlotRUD.as_view(), name = 'unavailableslot_list_rud'),
    path('unavailableslot-post' , UnavailableSlotCreate.as_view(), name='unavailableslot_post'),


    # transaction
    path('transaction', Transactionlist.as_view(), name = 'transaction_list'),
    path('transaction-rud/<int:pk>', TransactionRUD.as_view(), name = 'transaction_list_rud'),
    path('transaction-post' , TransactionCreate.as_view(), name='transaction_post'),

    
    # Token
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', getRoutes),
    

    # private endpoint
    path('test/', testEndPoint ,name='test'),

]


# urlpatterns += router.urls