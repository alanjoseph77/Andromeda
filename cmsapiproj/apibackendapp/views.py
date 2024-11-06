from rest_framework import viewsets,filters,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Appointment, Doctor, Patient
from .serializers import AppointmentSerializer, DoctorSerializer, PatientSerializer,LoginSerializer,BillSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import Bill
from .serializers import BillSerializer

from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['AppointmentDate']


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# Login API View - Authenticates users
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "username": user.username,
                    "role": user.groups.all()[0].id if user.groups.exists() else None,
                    "data": {
                        "Token": token.key
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid credentials"
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# class BillViewSet(viewsets.ModelViewSet):

#     permission_classes = [ AllowAny ]
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer

class BillViewSet(viewsets.ModelViewSet):

    permission_classes = [ AllowAny ]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def create(self, req):
        serializer = BillSerializer(data = req.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Bill generated successfully"
        }, status=status.HTTP_201_CREATED)
