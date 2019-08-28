from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ImportForm(forms.ModelForm):
    class Meta:
        model = Import
        fields = '__all__'

class ExportForm(forms.ModelForm):
    class Meta:
        model = Export
        fields = '__all__'
class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class BuildingWorksForm(forms.ModelForm):
    class Meta:
        model = BuildingWorks
        fields = '__all__'


class NegashaWorkForm(forms.ModelForm):
    class Meta:
        model = NegashaWork
        fields = '__all__'
        

class ElectricityWorkForm(forms.ModelForm):
    class Meta:
        model = ElectricityWork
        fields = '__all__'





class BayatWorkForm(forms.ModelForm):
    class Meta:
        model = BayatWork
        fields = '__all__'



class CebakaWorkForm(forms.ModelForm):
    class Meta:
        model = CebakaWork
        fields = '__all__'

class BulatWorkForm(forms.ModelForm):
    class Meta:
        model = BulatWork
        fields = '__all__'