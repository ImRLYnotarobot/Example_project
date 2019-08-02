def settings_context(request):
    from django.conf import settings
    return {'settings': settings}
