from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q


class ObjectListMixin:
    model = None
    template = None
    objects_per_page = None

    def get(self, request):

        page_number = request.GET.get('page', 1)
        sorted_query = self.model.get_sorted_query()

        load_name = '{}{}'.format(self.model.__name__.lower(), '_page')
        paginator = Paginator(sorted_query, self.objects_per_page)
        page = paginator.get_page(page_number)

        context = {
            load_name: page
        }

        return render(request, self.template, context=context)


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, id=None):
        if id:
            obj = get_object_or_404(self.model, id=id)
        else:
            return Http404()
        context = {
            self.model.__name__.lower(): obj
        }

        return render(request, self.template, context=context)


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        context = {
            'form': form,
        }
        return render(request, self.template, context=context)

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        else:
            return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, id=None):
        if id:
            obj = get_object_or_404(self.model, id=id)
        else:
            return Http404()
        bound_form = self.form_model(instance=obj)
        context = {
            'form': bound_form,
            self.model.__name__.lower(): obj,
            'action_url': reverse(
                self.model.__name__.lower()+'_update',
                kwargs={'id': obj.id}
            )
        }
        return render(request, self.template, context=context)

    def post(self, request, id=None):
        if id:
            obj = get_object_or_404(self.model, id=id)
        else:
            return Http404()
        bound_form = self.form_model(request.POST, instance=obj)
        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)
        else:
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj,
            }
            return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    template = None

    def get(self, request, id=None):
        if id:
            obj = get_object_or_404(self.model, id=id)
        else:
            return Http404()

        return render(request, self.template, context={
            self.model.__name__.lower(): obj
        })

    def post(self, request, id=None, slug=None):
        if id:
            obj = get_object_or_404(self.model, id=id)
        else:
            return Http404()

        redirect_url = obj.get_post_delete_url()

        obj.delete()

        return redirect(redirect_url)
