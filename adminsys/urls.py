from django.conf.urls import url
# Author gt401
from django.urls import path
from . import views

app_name='adminsys'

urlpatterns = [
      url('list_of_orders/', views.list_of_orders, name='list_of_orders'),
      path('list_of_jobs/<int:oid>/', views.list_of_jobs, name='list_of_jobs'),
      path('jobcard/<int:jcid>/', views.jobcard, name='jobcard'),
      path('operation_at_workstation/<int:opid>/<int:wid>/<int:jcid>/', views.operation_at_workstation, name='operation_at_workstation'),
      path('start_operation/', views.start_operation, name='start_operation'),
      path('end_operation/', views.end_operation, name='end_operation')
]
#      path('operation_at_workstation/<int:opid>/<int:wid>/<int:jcid>/', views.operation_at_workstation, {'foo': 'bar'}, name='operation_at_workstation')
