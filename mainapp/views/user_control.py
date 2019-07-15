from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.user_type ==2:
            return redirect('companies:home')
        elif request.user.user_type ==3:
            return redirect('department:home')
        else :
            return redirect('polus:home')
    return render(request, 'mainapp/home.html')
