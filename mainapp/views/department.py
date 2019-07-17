from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView

from ..forms import DepartmentSignUpForm
from ..models import  User


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
        return redirect('departments:home')

def home(request):
    return render(request,'mainapp/department/home.html')