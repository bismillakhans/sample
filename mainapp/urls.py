from django.urls import include, path

from .views import user_control,company,polus,department
urlpatterns = [
    path('', user_control.home, name='home'),

    path('company/', include(([

    # path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
    path('', company.home, name='home'),

                              ], 'user_control'), namespace='companies')),

    path('department/', include(([
        # path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
     path('', department.home, name='home'),
                                 ], 'user_control'), namespace='departments')),

    path('polus/', include(([
        # path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
    path('', polus.home, name='home'),
    path('createrule/', polus.RuleCreate.as_view(), name='rule_create'),

    ], 'user_control'), namespace='polus')),
]

