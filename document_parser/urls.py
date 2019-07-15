from django.urls import include, path

# from mainapp.views import user_control, department, company,polus
from mainapp.views import user_control, department, company, polus

urlpatterns = [
    path('', include('mainapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_control.SignUpView.as_view(), name='signup'),
    path('accounts/signup/department/', department.DepartmentSignUpView.as_view(), name='department_signup'),
    path('accounts/signup/company/', company.CompanySignUpView.as_view(), name='company_signup'),
    path('accounts/signup/polus/', polus.PolusSignUpView.as_view(), name='polus_signup'),
]
