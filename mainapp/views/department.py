from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ..forms import DepartmentSignUpForm, DepartmentRuleForm
from ..models import User, Department


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
        return redirect('department:home')

def uploadForm(request):
    return render(request,'mainapp/department/home.html')

def documentList(request):
    return render(request,'mainapp/department/document_list.html')

class DepartmentRuleView(UpdateView):
    model = Department
    form_class = DepartmentRuleForm
    template_name = 'mainapp/department/update_rule.html'
    success_url = reverse_lazy('department:home')

    def get_object(self):
        return self.request.user.department

    def form_valid(self, form):
        messages.success(self.request, 'Rules updated with success!')
        return super().form_valid(form)