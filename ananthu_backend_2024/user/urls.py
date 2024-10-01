from django.urls import path
from . import views

urlpatterns=[
    path('register',views.hashregister,name='hashregister'),
    path('login',views.login,name='login' ),
    path('logout',views.logouts,name='logouts' ),
    path('delete',views.deletedetails,name='delete'),
    path('display',views.displaydata,name='display'),
    path('search/<str:name>',views.serchdetails,name='serchdetails'),
    path('delete',views.deletedetails,name='deletedetails'),
    path('booking',views.BOOKINGS,name='bookingdetails'),
    path('doctor',views.doctor,name='doctor'),
    path('staff',views.staffs,name='staffs'),
    path('patient',views.patient,name='patient')
]