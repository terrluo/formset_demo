import json
import logging

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView


logger = logging.getLogger(__name__)


class SuccessMessageMixin(object):
    success_message = ''

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        print('xxxx')
        print('aaaa')
        return super(SuccessMessageMixin, self).get_success_url()


class FormSetMixin(object):
    formset_name = 'formset'
    formset_class = None

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        formset = self.formset_class(instance=self.object)
        return self.render_to_response(self.get_context_data(**{'form': form, self.formset_name: formset}))

    def post(self, request, *args, **kwargs):
        logger.info(json.dumps(request.POST, indent=4))

        form = self.get_form(self.get_form_class())
        formset = self.formset_class(self.request.POST, instance=self.object)

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(**{'form': form, self.formset_name: formset}))


class FormSetCreateView(SuccessMessageMixin, FormSetMixin, CreateView):
    action = '创建'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


class FormSetUpdateView(SuccessMessageMixin, FormSetMixin, UpdateView):
    action = '编辑'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
