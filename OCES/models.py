from django.db import models
from django.contrib.auth.models import *


# Create your models here.
class details_test(models.Model):
    # entry_no=models.AutoField()
    # entry_number=models.AutoField(primary_key=True,default=0)
    subject= models.CharField(max_length=30)
    num_of_ques= models.PositiveIntegerField()
    candidate_name =models.CharField(max_length=20)

    # def show_sub(self):
    #     return 

    def show_record(self):
        # return str(str(self.num_of_ques),(self.candidate_name)) # hel = details_test.objects.earliest('num_of_ques').values_list()
        NOQ =details_test.objects.values_list().last()  #getting latest value in list format
        return NOQ #.values_list()        # return hel

    def __str__(self):
        return '{} {}'.format(self.candidate_name,self.num_of_ques)

    # def __int__(self):
    #     return self.num_of_ques


class details_answers(models.Model):
    option_selected=models.CharField(max_length=10)
    
    def __str__(self):
        return self.option_selected

    def show_entered_ans(self):
        return details_answers.objects.values_list().last() 

    