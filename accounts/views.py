from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import ProfileForm1, ProfileForm2
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from formtools.wizard.views import SessionWizardView
from accounts.models import User, UserProfile

# Create your views here.
class FormWizardView(SessionWizardView):
    template_name = "accounts/register.html"
    form_list = [ProfileForm1, ProfileForm2]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {'form_data': [form.cleaned_data for form in form_list]})
