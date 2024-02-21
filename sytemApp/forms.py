from django import forms
from .models import Group, Member

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['representative_name', 'representative_email']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_name', 'member_email']
        widgets = {
            'name': forms.TextInput(attrs={'required': False}),
            'email': forms.EmailInput(attrs={'required': False}),
        }
