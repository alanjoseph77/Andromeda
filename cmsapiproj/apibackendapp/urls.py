from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, DoctorViewSet, PatientViewSet
from . import views
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')
# router.register(r'billing',views.BillViewSet)
router.register(r'billing',views.BillViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# router.register(r'employees',views.AppointmentViewSet)
# router.register(r'department',views.DoctorViewSet)
# router.register(r'user',views.PatientViewSet)



urlpatterns = [
    
    path("login/", views.LoginAPIView.as_view(), name="user-login"),
    ]

urlpatterns += router.urls
