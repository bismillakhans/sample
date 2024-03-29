from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import polus_required, company_required
from ..forms import CompanySignUpForm, RuleModelForm, DepartmentSignUpForm
from ..models import User, Rule



@login_required
@company_required
def homePage(request):
    return render(request,'mainapp/company/home.html')

@method_decorator([login_required, company_required], name='dispatch')
class RuleCreate(CreateView):
    model = Rule
    form_class = RuleModelForm
    template_name = 'mainapp/polus/rule_create.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The Rule created successfully')
        return redirect('company:homePage')

@method_decorator([login_required, company_required], name='dispatch')
class DepartmentSignUpView(CreateView):
    model = User
    form_class = DepartmentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'department'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The Department created successfully')
        return redirect('company:homePage')
