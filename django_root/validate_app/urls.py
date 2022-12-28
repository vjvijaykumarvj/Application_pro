from django.urls import path,include
from.import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee_validate',views.Employee_Validate,basename='employee_validate')


urlpatterns=[
    path('',include(router.urls))
]