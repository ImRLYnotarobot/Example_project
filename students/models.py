from django.db import models
from django.db.models import Count
from django.shortcuts import reverse


class Group(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    headman = models.ForeignKey(
        'Student',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        student_count = self.student_set.count()
        return '{} [{}]'.format(self.name, student_count)

    @classmethod
    def get_sorted_query(cls):
        return cls.objects.annotate(
            total_students=Count('student')
        ).order_by('-total_students')

    def students(self):
        return self.student_set.all()

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('group_update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('group_delete', kwargs={'id': self.id})

    def get_post_delete_url(self):
        return reverse('group_list')


class Student(models.Model):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    middle_name = models.CharField(max_length=128, blank=True)
    birth_d = models.DateField(verbose_name='Birth date')
    group_id = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Group',
    )

    def short_name(self):
        if self.middle_name:
            return '{} {}.{}.'.format(
                self.last_name,
                self.first_name[0],
                self.middle_name[0]
            )
        else:
            return '{} {}.'.format(
                self.last_name,
                self.first_name[0]
            )

    def is_headman(self):
        if self.group_set.all():
            return True
        else:
            return False

    is_headman.boolean = True
    short_name.short_description = 'Name'
    # self.group_id.short_description = 'Group'

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('student_update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('student_delete', kwargs={'id': self.id})

    def get_post_delete_url(self):
        return self.group_id.get_absolute_url()


class Log(models.Model):
    ACTIONS = [
        ('CR', 'Created'),
        ('CD', 'Changed'),
        ('DL', 'Deleted')
    ]

    action = models.CharField(blank=False, max_length=2, choices=ACTIONS)
    model_name = models.CharField(max_length=127)
    object_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.action == 'CR':
            message = 'Created'
        elif self.action == 'CD':
            message = 'Changed'
        elif self.action == 'DL':
            message = 'Deleted'
        return '{} {} object'.format(message, self.model_name.lower())
