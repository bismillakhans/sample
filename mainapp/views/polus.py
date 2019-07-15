from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView

from ..forms import PolusSignUpForm
from ..models import  User


class PolusSignUpView(CreateView):
    model = User
    form_class = PolusSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'polus'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('polus:home')


def home(request):
    return render(request,'mainapp/polus/home.html')