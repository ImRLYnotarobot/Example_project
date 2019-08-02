from django import template
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def admin_edit(obj):
    inf = obj._meta
    template = '<a href="{}">admin edit page</a>'

    link = '/admin/{}/{}/{}/change/'.format(
        inf.app_label,
        inf.model_name,
        obj.pk
    )

    return mark_safe(template.format(link))
