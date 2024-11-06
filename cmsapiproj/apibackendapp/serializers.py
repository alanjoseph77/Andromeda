from rest_framework import serializers
from .models import Doctor, Patient, Appointment,Bill
from django.contrib.auth.models import Group, User



class DoctorSerializer(serializers.ModelSerializer):
    SpecializationName = serializers.CharField(source='SpecializationId.SpecializationName', read_only=True)
    FullName = serializers.CharField(source='StaffId.FullName', read_only=True)

    class Meta:
        model = Doctor
        fields = ['DoctorId', 'FullName', 'ConsultationFee', 'IsActive', 'SpecializationId', 'SpecializationName']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


# Login Serializer
class LoginSerializer(serializers.ModelSerializer): 
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


# class BillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bill
#         fields = [ 'AppointmentId', 'amount', 'description' ]



class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'