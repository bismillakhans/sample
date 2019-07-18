import os
from . import utils_second
import spacy
from django.conf import settings


class ResumeParser(object):
    def __init__(self, resume):



        self.__details = {
            'name'              : None,
            'email'             : None,
            'mobile_number'     : None,
            'skills': None,
            'full_data': None,
            'declaration': None,
            'achievements': None,
            'education': None,
            'experience': None,
            'experience_json': None,
            'hobbies': None,
            'interest': None,
            'language': None,
            'objective': None,
            'personal_details': None,
            'personal_details_json': None,
            'project': None,
            'project_json': None,
            'reference': None,
            'seminar': None,
            'soft_skill': None,
            'technical_skill': None,
            'technical_skill_json': None,
            'iv': None,
            'training': None

        }
        self.__resume = resume
        # self.__result=[]
        # self.__text_raw = utils.extract_text(self.__resume, os.path.splitext(self.__resume)[1])#put resumes with removing extension
        self.__result=utils_second.function1(self.__resume)
        self.final__result=utils_second.final_result(self.__result)
        print(self.final__result)
        self.nlp_model_pd = spacy.load(settings.PD_MODEL_PATH)
        self.nlp_model_proj = spacy.load(settings.PROJ_MODEL_PATH)
        self.nlp_model_exp = spacy.load(settings.EXP_MODEL_PATH)
        self.nlp_model_tech = spacy.load(settings.TECH_MODEL_PATH)



        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details
    def __get_basic_details(self):
        # name=utils.extract_name(self.__nlp_model)
        # mobile=utils_second.extract_mobile_number(self.__text)
        # email=utils_second.extract_email(self.__text)
        self.__details['full_data'] = self.final__result

        try:
            exp = self.final__result['experience']
            self.__details['experience'] = exp
            _exp = self.nlp_model_exp(exp)
            exp_name = utils_second.extract_name(_exp)
            self.__details['experience_json'] = exp_name
            print(exp_name)
            # try:
            #     self.__details['name'] = pd_name['name']
            # except:
            #     self.__details['name'] = "No name found"
        except:
            self.__details['experience'] = "No experience found"
        try:
            self.__details['skills'] = self.final__result['skills']
        except:
            self.__details['skills'] = "No skills found"
        try:
            self.__details['declaration'] = self.final__result['declaration']
        except:
            self.__details['declaration'] = "No declaration found"
        try:
            self.__details['achievements'] = self.final__result['achievements']
        except:
            self.__details['achievements'] = "No achievements found"
        try:
            self.__details['education'] = self.final__result['education']
        except:
            self.__details['education'] = "No education found"
        try:
            self.__details['hobbies'] = self.final__result['hobbies']
        except:
            self.__details['hobbies'] = "No hobbies found"
        try:
            self.__details['interest'] = self.final__result['interest']
        except:
            self.__details['interest'] = "No interest found"
        try:
            self.__details['language'] = self.final__result['language']
        except:
            self.__details['language'] = "No language found"
        try:
            self.__details['objective'] = self.final__result['objective']
        except:
            self.__details['objective'] = "No objective found"
        try:
            pd=self.final__result['personal detail']
            _name=self.nlp_model_pd(pd)
            pd_name= utils_second.extract_name(_name)
            self.__details['personal_details'] = pd
            self.__details['personal_details_json'] = pd_name
            print(pd_name)
            try:
                self.__details['name'] =  pd_name['name']
            except:
                self.__details['name'] = "No name found"
            try:
                self.__details['email'] = pd_name['email']
            except:
                self.__details['email'] = "No email found"
            try:
                self.__details['mobile_number'] = pd_name['contact_no']
            except:
                self.__details['mobile_number'] = "No mobile_number found"


        except:
            self.__details['personal_details'] = "No personal details found"
        try:
            self.__details['project'] =proj= self.final__result['project']
            _proj = self.nlp_model_proj(proj)
            proj_name = utils_second.extract_name(_proj)
            self.__details['project_json'] = proj_name
            print(proj_name)
        except:
            self.__details['project'] = "No project found"
        try:
            self.__details['language'] = self.final__result['language']
        except:
            self.__details['language'] = "No language found"
        try:
            self.__details['reference'] = self.final__result['reference']
        except:
            self.__details['reference'] = "No reference found"
        try:
            self.__details['seminar'] = self.final__result['seminar']
        except:
            self.__details['seminar'] = "No seminar found"
        try:
            self.__details['soft_skill'] = self.final__result['soft_skill']
        except:
            self.__details['soft_skill'] = "No soft_skill found"
        try:

            tech = self.final__result['technical skill']
            self.__details['technical_skill'] =tech
            _tech = self.nlp_model_tech(tech)
            tech_name = utils_second.extract_name(_tech)
            self.__details['technical_skill_json'] = tech_name
            print(tech_name)
        except:
            self.__details['technical_skill'] = "No technical_skill found"
        try:
            self.__details['training'] = self.final__result['training']
        except:
            self.__details['training'] = "No training found"
        try:
            self.__details['iv'] = self.final__result['iv']
        except:
            self.__details['iv'] = "No iv found"
        return
