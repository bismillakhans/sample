from django.urls import include, path

from .views import user_control,company,polus,department
urlpatterns = [
    path('', user_control.home, name='home'),

    path('company/', include(([

    path('', company.homePage, name='homePage'),
    path('createrule/', company.RuleCreate.as_view(), name='rule_create'),

                              ], 'user_control'), namespace='company')),

    path('department/', include(([
     path('uploadForm/', department.uploadForm, name='uploadForm'),
     path('', department.documentList, name='document_list'),
    path('interests/', department.DepartmentRuleView.as_view(), name='update_rules'),
                                 ], 'user_control'), namespace='department')),

    path('polus/', include(([
    path('', polus.homePage, name='homePage'),
    path('polusSignup/', polus.PolusSignUpView.as_view(), name='polus_signup'),

    ], 'user_control'), namespace='polus')),
]

