from django.shortcuts import reverse, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import (
    ObjectListMixin,
    ObjectDetailMixin,
    ObjectCreateMixin,
    ObjectUpdateMixin,
    ObjectDeleteMixin,
    BasicLoginRequiredMixin,
)
from .models import Group, Student
from .forms import (
    GroupForm,
    StudentForm,
    GroupUpdateForm,
    StudentUpdateForm,
)


class GroupCreateView(BasicLoginRequiredMixin, ObjectCreateMixin, View):
    form_model = GroupForm
    template = 'students/group_create.html'


class GroupListView(ObjectListMixin, View):
    model = Group
    objects_per_page = 4
    template = 'students/group_list.html'


class GroupDetailView(ObjectDetailMixin, View):
    model = Group
    template = 'students/group_detail.html'


class GroupUpdateView(BasicLoginRequiredMixin, ObjectUpdateMixin, View):
    model = Group
    form_model = GroupUpdateForm
    template = 'students/group_update.html'


class GroupDeleteView(BasicLoginRequiredMixin, ObjectDeleteMixin, View):
    model = Group
    template = 'students/group_delete.html'


class StudentDetailView(BasicLoginRequiredMixin, ObjectDetailMixin, View):
    model = Student
    template = 'students/student_detail.html'


class StudentCreateView(BasicLoginRequiredMixin, ObjectCreateMixin, View):
    form_model = StudentForm
    template = 'students/student_create.html'

    def get(self, request):
        '''
        changes behavior in order to
        take "from" get parameter which represents refer gorup
        for pretty form render
        '''
        init_group_id = request.GET.get('from', None)
        init_group = None

        if init_group_id:
            queryset = Group.objects.filter(id=init_group_id)
            if queryset.exists():
                init_group = queryset[0]

        form = self.form_model()
        form.fields['group_id'].initial = init_group    # set 'selected' to refer group
        context = {
            'form': form,
        }
        return render(request, self.template, context=context)


class StudentUpdateView(BasicLoginRequiredMixin, ObjectUpdateMixin, View):
    model = Student
    form_model = StudentUpdateForm
    template = 'students/student_update.html'


class StudentDeleteView(BasicLoginRequiredMixin, ObjectDeleteMixin, View):
    model = Student
    template = 'students/student_delete.html'
