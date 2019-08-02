from django.shortcuts import reverse
from django.views.generic import View

from .utils import (
    ObjectListMixin,
    ObjectDetailMixin,
    ObjectCreateMixin,
    ObjectUpdateMixin,
    ObjectDeleteMixin,
)
from .models import Group, Student
from .forms import (
    GroupForm,
    StudentForm,
    GroupUpdateForm,
    StudentUpdateForm,
)


class GroupCreateView(ObjectCreateMixin, View):
    form_model = GroupForm
    template = 'students/group_create.html'


class GroupListView(ObjectListMixin, View):
    model = Group
    objects_per_page = 4
    template = 'students/group_list.html'


class GroupDetailView(ObjectDetailMixin, View):
    model = Group
    template = 'students/group_detail.html'


class GroupUpdateView(ObjectUpdateMixin, View):
    model = Group
    form_model = GroupUpdateForm
    template = 'students/group_update.html'


class GroupDeleteView(ObjectDeleteMixin, View):
    model = Group
    template = 'students/group_delete.html'


class StudentDetailView(ObjectDetailMixin, View):
    model = Student
    template = 'students/student_detail.html'


class StudentCreateView(ObjectCreateMixin, View):
    form_model = StudentForm
    template = 'students/student_create.html'


class StudentUpdateView(ObjectUpdateMixin, View):
    model = Student
    form_model = StudentUpdateForm
    template = 'students/student_update.html'


class StudentDeleteView(ObjectDeleteMixin, View):
    model = Student
    template = 'students/student_delete.html'
