from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
# from document_parser import resume_parser
from ..decorators import company_required,department_required
from ..forms import DepartmentSignUpForm, DepartmentRuleForm, UploadResumeModelForm
from ..models import User, Department, Resume
import os

from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse



@login_required
@department_required
def uploadForm(request):
    if request.method == 'POST':
        file_form = UploadResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')
        # resumes_data = []
        if file_form.is_valid():
            for file in files:
                try:
                    # saving the file
                    user = request.user

                    # saving the file
                    resume = Resume(user=user, resume=file)
                    resume.save()

                    # parser = resume_parser.ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.resume.name))
                    # data = parser.get_extracted_data()
                    # resume.education = data.get("education")
                    # resume.experience = "experience"
                    #
                    # resume.experience = data.get('experience')
                    # resume.experience_json = data.get('experience_json')
                    # resume.name = data.get('name')
                    # resume.email = data.get('email')
                    # resume.mobile_number = data.get('mobile_number')
                    # resume.project = data.get('project')
                    # resume.project_json = data.get('project_json')
                    # resume.skills = data.get('skills')
                    # resume.full_data = data.get('full_data')
                    # resume.objective = data.get('objective')
                    # resume.seminar = data.get('seminar')
                    # resume.technical_skill = data.get('technical_skill')
                    # resume.technical_skill_json = data.get('technical_skill_json')
                    # resume.soft_skill = data.get('soft_skill')
                    # resume.skills = data.get('skills')
                    # resume.personal_details = data.get('personal_details')
                    # resume.personal_details_json = data.get('personal_details_json')
                    # resume.reference = data.get('reference')
                    # resume.interest = data.get('interest')
                    # resume.save()
                    # messages.SUCCESS(request,"File Successfully Uploaded")
                    return redirect('department:document_list')
                except IntegrityError:
                    HttpResponse("error found")
    else:
        form = UploadResumeModelForm()
    return render(request, 'mainapp/department/home.html', {
        'form': form
    })






@login_required
@department_required
def documentList(request):
    return render(request,'mainapp/department/document_list.html')

@method_decorator([login_required, department_required], name='dispatch')
class DepartmentRuleView(UpdateView):
    model = Department
    form_class = DepartmentRuleForm
    template_name = 'mainapp/department/update_rule.html'
    success_url = reverse_lazy('department:uploadForm')

    def get_object(self):
        return self.request.user.department

    def form_valid(self, form):
        messages.success(self.request, 'Rules updated with success!')
        return super().form_valid(form)