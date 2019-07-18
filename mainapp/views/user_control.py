from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..forms import RuleModelForm

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'




def home(request):
    if request.user.is_authenticated:
        if request.user.user_type ==2:
            return redirect('company:homePage')
        elif request.user.user_type ==3:
            return redirect('department:document_list')
        else :
            return redirect('polus:homePage')

    return render(request, 'mainapp/home.html')
