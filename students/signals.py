from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, Group, Log


@receiver(post_save, sender=Group)
@receiver(post_save, sender=Student)
def post_save_callback(sender, instance, **kwargs):
    if kwargs['created']:
        action = 'CR'   # created
    else:
        action = 'CD'   # changed

    new_log = create_log(instance, action)
    print(new_log)


@receiver(post_delete, sender=Group)
@receiver(post_delete, sender=Student)
def post_delete_callback(sender, instance, **kwargs):
    action = 'DL'       # deleted
    new_log = create_log(instance, action)
    print(new_log)


def create_log(instance, action):
    new_log = Log(
        action=action,
        model_name=instance.__class__.__name__,
        object_id=instance.id
    )
    new_log.save()
    return new_log
