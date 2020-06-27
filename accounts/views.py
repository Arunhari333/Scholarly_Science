from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import ProfileForm1, ProfileForm2
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User, register, detail
from django.views.generic import TemplateView

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

            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            Email = form.cleaned_data['Email']
            Mobile = form.cleaned_data['Mobile']
            City = form.cleaned_data['City']
            College = form.cleaned_data['College']
            Degree = form.cleaned_data['Degree']
            Major = form.cleaned_data['Major']
            StartDate = form.cleaned_data['StartDate']
            EndDate = form.cleaned_data['EndDate']

            #return redirect('/account/profile/')
            args = {'FirstName': FirstName, 'LastName': LastName, 'Email': Email, 'Mobile': Mobile,
                    'City': City, 'College': College, 'Degree': Degree, 'Major': Major,
                    'StartDate': StartDate, 'EndDate': EndDate}
            return render(request, self.template_name, args)

O = RegView()

def Profile(request):
    # form = ProfileForm1(request.POST)
    if request.user.is_authenticated:
        if register.objects.filter(user=request.user).exists():
            # return redirect('/account/company-url/')
            details = register.objects.get(user=request.user)
            args = {'data': details, 'id': request.user.id}
            return render(request, 'accounts/details.html', args)

        else:
            if request.method == 'POST':
                return O.post(request)
            else:
                return O.get(request)

class Detail(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/detail.html'

    def get(self, request):
        form = ProfileForm2()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm2(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user2 = request.user
            instance.save()

            return redirect('/account/company-url/')

