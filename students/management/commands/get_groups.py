from django.core.management.base import BaseCommand
from students.models import Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for group in Group.objects.all():
            self.stdout.write(str(group), ending=':\n')
            students = group.student_set.all()
            if students.exists():
                for student in group.student_set.all():
                    self.stdout.write('\t'+str(student))
            else:
                self.stdout.write('\tno students')
