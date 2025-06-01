from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Attendance, PerformanceRecord
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceRecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg

class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department__name']
    search_fields = ['first_name', 'last_name', 'email']

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceList(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'date', 'status']

class PerformanceRecordList(generics.ListAPIView):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'review_date']

class PerformanceSummary(APIView):
    def get(self, request):
        data = (
            PerformanceRecord.objects.values('employee__first_name', 'employee__last_name')
            .annotate(avg_rating=Avg('rating'))
        )
        return Response(data)
    from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([AllowAny])
def performance_chart_view(request):
    return render(request, 'visualization.html')

