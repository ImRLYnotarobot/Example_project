from django import forms

from .models import Group, Student


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Group name'
                }
            ),
        }


class GroupUpdateForm(forms.ModelForm):
    unregistered_students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.filter(group_id=None),
        required=False
    )

    class Meta:
        model = Group
        fields = ['name', 'headman', 'unregistered_students']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].queryset = self.instance.student_set.all()

    def save(self, *args, **kwargs):
        updated_group = super().save(*args, **kwargs)
        if self.cleaned_data['unregistered_students'].exists():
            for student in self.cleaned_data['unregistered_students']:
                student.group_id = updated_group
                student.save()
        return updated_group


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'birth_d',
            'group_id'
        ]
        widgets = {
            'birth_d': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
