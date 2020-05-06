from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','emp_code','mobile','position')      #you can also assign the '__all__' to fields so that all the columns from tables are assigned
        labels ={
            'fullname':'Full Name',
            'emp_code': 'EMP Code'
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False