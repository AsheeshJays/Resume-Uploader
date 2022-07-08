from django import forms
from .models import Resume

GENDER_CHOICE = [
    ('male', 'Male'),
    ('female', 'Female')
]

JOB_CITY_CHOICE = [
    ('Delhi','Delhi'),
    ('Noida','Noida'),
    ('Gurugram','Gurugram'),
    ('Pune','Pune'),
    ('Banglore','Banglore'),
    ('Hydrabad','Hydrabad'),
    ('Chenni','Chenni')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferd Job Location',choices=JOB_CITY_CHOICE,
    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city',
        'pin','state','mobile','email','job_city','profile_image','my_file']

        labels = {'name':'Full Name','dob':'Date Of Birth','pin':'Pin Code',
        'mobile':'Mobile No.','email':'Email ID', 'job_city':'Job City','profile_image':'Profile Image','my_file':'Document'}
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }