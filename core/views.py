from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import BaseCreateView, BaseUpdateView


class FormSetMixin(object):
    formset_name = 'formset'
    formset_class = None

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        formset = self.formset_class(instance=self.object)
        return self.render_to_response(self.get_context_data(**{'form': form, self.formset_name: formset}))

    def post(self, request, *args, **kwargs):
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
        return self.render_to_response(**{'form': form, self.formset_name: formset})


class FormSetCreateView(SingleObjectTemplateResponseMixin, FormSetMixin, BaseCreateView):
    action = '创建'
    template_name_suffix = '_form'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


class FormSetUpdateView(SingleObjectTemplateResponseMixin, FormSetMixin, BaseUpdateView):
    action = '编辑'
    template_name_suffix = '_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
