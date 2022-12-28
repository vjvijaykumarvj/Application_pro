from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'employee_app'


urlpatterns=[
    path('employee_dashboard/',views.EmployeeDashboard),
    path('employee_update/<pk>',views.employee_update,name='employee_update'),
    path('employee_delete/<pk>',views.employee_delete,name='employee_delete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)