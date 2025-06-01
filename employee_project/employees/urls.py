from django.urls import path
from .views import EmployeeList, EmployeeDetail, AttendanceList, PerformanceRecordList, PerformanceSummary

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    path('performance/', PerformanceRecordList.as_view(), name='performance-list'),
    path('performance/summary/', PerformanceSummary.as_view(), name='performance-summary'),
]
from .views import performance_chart_view

urlpatterns += [
    path('performance/chart/', performance_chart_view, name='performance-chart'),
]
