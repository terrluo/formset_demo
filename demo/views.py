from django.contrib import messages
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView

from core.views import FormSetCreateView, FormSetUpdateView
from demo.forms import CompanyForm, EmployeeForm
from demo.models import Company, Employee


class IndexView(TemplateView):
    template_name = 'demo/index.html'


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'demo/company_list.html'


class CompanyCreateView(FormSetCreateView):
    model = Company
    context_object_name = 'company'
    form_class = CompanyForm
    success_message = '创建成功'
    success_url = reverse_lazy('demo:company_list')
    template_name = 'demo/company_create_or_update.html'
    formset_name = 'employee_forms'
    formset_class = inlineformset_factory(
        parent_model=Company,
        model=Employee,
        form=EmployeeForm,
        can_delete=False,
        extra=1,
    )

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super(CompanyCreateView, self).get_success_url()


class CompanyUpdateView(FormSetUpdateView):
    model = Company
    context_object_name = 'company'
    form_class = CompanyForm
    pk_url_kwarg = 'company_id'
    success_message = '修改成功'
    success_url = reverse_lazy('demo:company_list')
    template_name = 'demo/company_create_or_update.html'
    formset_name = 'employee_forms'
    formset_class = inlineformset_factory(
        parent_model=Company,
        model=Employee,
        form=EmployeeForm,
        can_delete=True,
        extra=1,
    )


class CompanyDeleteVieW(DeleteView):
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'
    success_message = '删除成功'
    success_url = reverse_lazy('demo:company_list')
    template_name = 'demo/company_delete.html'
