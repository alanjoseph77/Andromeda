from django.contrib import admin
from .models import Appointment,Patient,Doctor,Membership,Specialization,Staff,Role,Bill
from rest_framework.authtoken.models import Token
# from .models import (
#     Role, Staff, Specialization, Doctor, Membership, Patient, 
#     Appointment, MedicineCategory, Medicine, MedicinePrescription, 
#     Consultation, MedicineStock, LabTestCategory, LabTest, LabTestPrescription
# )



admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Membership)
admin.site.register(Specialization)
admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(Bill)
# admin.site.register(Token)
# # Admin for Role model
# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('RoleId', 'RoleName', 'IsActive')
#     search_fields = ('RoleName',)
#     list_filter = ('IsActive',)

# # Admin for Staff model
# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('StaffId', 'FullName', 'Gender', 'MobileNumber', 'RoleId', 'IsActive')
#     search_fields = ('FullName', 'UserName')
#     list_filter = ('RoleId', 'IsActive')

# # Admin for Specialization model
# @admin.register(Specialization)
# class SpecializationAdmin(admin.ModelAdmin):
#     list_display = ('SpecializationId', 'SpecializationName')
#     search_fields = ('SpecializationName',)

# # Admin for Doctor model with Specialization and Staff details
# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ('DoctorId', 'get_full_name', 'get_specialization', 'ConsultationFee', 'IsActive')
#     search_fields = ('StaffId__FullName', 'SpecializationId__SpecializationName')
#     list_filter = ('SpecializationId', 'IsActive')

#     # Display full name of doctor from related Staff
#     def get_full_name(self, obj):
#         return obj.StaffId.FullName
#     get_full_name.short_description = 'Doctor Name'

#     # Display specialization name from related Specialization
#     def get_specialization(self, obj):
#         return obj.SpecializationId.SpecializationName
#     get_specialization.short_description = 'Specialization'

# # Admin for Membership model
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ('MembershipId', 'MembershipType', 'IsActive')
#     search_fields = ('MembershipType',)
#     list_filter = ('IsActive',)

# # Admin for Patient model
# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('PatientId', 'PatientName', 'DateOfBirth', 'MobileNumber', 'MembershipId', 'IsActive')
#     search_fields = ('PatientName', 'MobileNumber')
#     list_filter = ('MembershipId', 'IsActive')

# # Admin for Appointment model
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('AppointmentId', 'AppointmentDate', 'PatientId', 'DoctorId', 'ConsultationStatus', 'IsActive')
#     search_fields = ('PatientId__PatientName', 'DoctorId__StaffId__FullName')
#     list_filter = ('ConsultationStatus', 'IsActive')

# # Admin for MedicineCategory model
# @admin.register(MedicineCategory)
# class MedicineCategoryAdmin(admin.ModelAdmin):
#     list_display = ('MedicineCategoryId', 'MedicineCategoryName')
#     search_fields = ('MedicineCategoryName',)

# # Admin for Medicine model
# @admin.register(Medicine)
# class MedicineAdmin(admin.ModelAdmin):
#     list_display = ('MedicineId', 'MedicineName', 'ManufacturingDate', 'ExpiryDate', 'Unit', 'MedicineCategoryId', 'IsActive')
#     search_fields = ('MedicineName',)
#     list_filter = ('MedicineCategoryId', 'IsActive')

# # Admin for MedicinePrescription model
# @admin.register(MedicinePrescription)
# class MedicinePrescriptionAdmin(admin.ModelAdmin):
#     list_display = ('MedicinePrescriptionId', 'MedicineId', 'Dosage', 'Frequency', 'Duration', 'AppointmentId', 'IsActive')
#     search_fields = ('MedicineId__MedicineName', 'AppointmentId__AppointmentId')

# # Admin for Consultation model
# @admin.register(Consultation)
# class ConsultationAdmin(admin.ModelAdmin):
#     list_display = ('ConsultationId', 'Symptoms', 'Diagnosis', 'Notes', 'CreatedDate', 'AppointmentId', 'IsActive')
#     search_fields = ('Symptoms', 'Diagnosis')

# # Admin for MedicineStock model
# @admin.register(MedicineStock)
# class MedicineStockAdmin(admin.ModelAdmin):
#     list_display = ('MedicineStockId', 'StockInHand', 'ReOrderLevel', 'Purchase', 'Issuance', 'MedicineId', 'CreatedDate', 'IsActive')
#     search_fields = ('MedicineId__MedicineName',)

# # Admin for LabTestCategory model
# @admin.register(LabTestCategory)
# class LabTestCategoryAdmin(admin.ModelAdmin):
#     list_display = ('LabTestCategoryId', 'LabTestCategoryName')
#     search_fields = ('LabTestCategoryName',)

# # Admin for LabTest model
# @admin.register(LabTest)
# class LabTestAdmin(admin.ModelAdmin):
#     list_display = ('LabTestId', 'TestName', 'Amount', 'ReferenceMinRange', 'ReferenceMaxRange', 'SampleRequired', 'LabTestCategoryId', 'IsActive')
#     search_fields = ('TestName',)
#     list_filter = ('LabTestCategoryId', 'IsActive')

# # Admin for LabTestPrescription model
# @admin.register(LabTestPrescription)
# class LabTestPrescriptionAdmin(admin.ModelAdmin):
#     list_display = ('LabTestPrescriptionId', 'LabTestId', 'LabTestValue', 'CreatedDate', 'Remarks', 'AppointmentId', 'IsActive')
#     search_fields = ('LabTestId__TestName', 'AppointmentId__AppointmentId')
