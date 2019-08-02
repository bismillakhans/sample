from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..forms import PolusSignUpForm, RuleModelForm, CompanySignUpForm
from ..models import  User,Rule
from ..decorators import polus_required

class PolusSignUpView(CreateView):
    model = User
    form_class = PolusSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'polus'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'The Polus created successfully')
        login(self.request, user)
        return redirect('polus:homePage')

@login_required
@polus_required
def homePage(request):
    return render(request,'mainapp/polus/home.html')


@method_decorator([login_required, polus_required], name='dispatch')
class RuleCreate(CreateView):
    model = Rule
    form_class = RuleModelForm
    template_name = 'mainapp/polus/rule_create.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The Rule created successfully')
        return redirect('polus:homePage')



@method_decorator([login_required, polus_required], name='dispatch')
class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'The company created successfully')
        # login(self.request, user)
        return redirect('polus:homePage')
