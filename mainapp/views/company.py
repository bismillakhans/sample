from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView

from ..forms import CompanySignUpForm
from ..models import  User


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
        login(self.request, user)
        return redirect('company:home')


def home(request):
    return render(request,'mainapp/company/home.html')