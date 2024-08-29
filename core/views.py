from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .models import Service, Employee, Feature
from .forms import ContactForm
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['features'] = Feature.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail successfully sent!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error while trying to send the e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
class LearnMoreView(TemplateView):
    template_name = 'learn.html'

