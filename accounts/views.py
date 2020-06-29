from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import ProfileForm1, ProfileForm2
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User, register, detail
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
class RegView(TemplateView):
    template_name = 'accounts/register.html'

    def get(self, request):
        form = ProfileForm1()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm1(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/account/')
        else:
            try:
                Mobile = form.cleaned_data['Mobile']
            except:
                messages.error(request, 'Enter proper mobile number (Without Space)')
            try:
                Email = form.cleaned_data['Email']
            except:
                messages.error(request, 'Enter proper email id')
            if not messages:
                messages.error(request, 'Enter proper email id and mobile number')
            return render(request, self.template_name, {'form': form})

O = RegView()

@login_required
def Profile(request):
    if request.user.is_authenticated:
        if register.objects.filter(user=request.user).exists():
            if detail.objects.filter(user=request.user).exists():
                return redirect('/account/company-url/')
            else:
                return redirect('/account/detail/')
        else:
            if request.method == 'POST':
                return O.post(request)
            else:
                return O.get(request)
    else:
        pass

class Detail(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/detail.html'

    def get(self, request):
        if register.objects.filter(user=request.user).exists():
            if detail.objects.filter(user=request.user).exists():
                return redirect('/account/')
            else:
                form = ProfileForm2()
                return render(request, self.template_name, {'form': form})
        else:
            return redirect('/account/')

    def post(self, request):
        form = ProfileForm2(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('/account/company-url/')

@login_required
def company_page(request):
    if register.objects.filter(user=request.user).exists() and detail.objects.filter(user=request.user).exists():
        return render(request, 'accounts/company-page.html')
    else:
        return redirect('/account/')
