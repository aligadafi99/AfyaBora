from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('dashboard', views.dashboard , name="dashboard"),
    path('admin_panel', views.admin_panel , name="admin_panel"),
    path('admin_login', views.admin_login , name="admin_login"),
    path('signUp',views.signUp,name = 'signUp'),
    path('login',views.login,name = 'login'),
    path('signout',views.signout,name = 'signout'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('add_appointment', views.add_appointment, name='add_appointment'),
    path('view_appointment', views.view_appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>', views.Delete_Appointment, name='delete_appointment'),
    path('view_patient', views.view_patient, name='view_patient'),
    path('edit_patient/<int:pid>',views.edit_patient,name='edit_patient'),
    path('delete_patient/<int:pid>', views.Delete_Patient, name='delete_patient'),
    path('edit_doctor/<int:pid>', views.edit_doctor,name='edit_doctor'),
    path('add_doctor', views.add_doctor, name='add_doctor'),####
    path('view_doctor', views.view_doctor, name='view_doctor'),####
    path('delete_doctor/<int:pid>', views.Delete_Doctor, name='delete_doctor'),
    path('choose-doctor/', views.choose_doctor, name='choose_doctor'),
    path("bill",views.order,name = "bill"),
    
    
]


