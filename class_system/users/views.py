from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import CustomForm
from .models import CustomUser
from classes.models import Enrollments
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

def Home(request):
    return redirect('login')

def Register(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account has been created, now you are able to log in.')
            return redirect('login')
    else:
        form = CustomForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def Profile(request):
    if request.method == 'POST':
        user_form = CustomForm(request.POST, instance=request.user)
        if user_form.is_valid():
            queryset = Enrollments.objects.filter(student=request.user)
            if queryset.exists():
                is_matched = False
                for obj in queryset:
                    if obj.class_enrolled.age_group == request.user.age:
                        is_matched = True
                    else:
                        is_matched = False
                if is_matched:
                    user_form.save()
                    messages.success(request, f'Your profile has been updated.')
                if not is_matched:
                    messages.error(request, f'You have enrolled in classes that do not match your updated age group. Please check again.')
                    user_form = CustomForm(instance=request.user)
            else:
                user_form.save()
                messages.success(request, f'Your profile has been updated.')
    else:
        user_form = CustomForm(instance=request.user)

    return render(request, 'users/profile.html', {'user_form': user_form})

class UserEnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollments
    template_name = 'users/enrollment_record.html'
    
    def get_queryset(self):
        context = Enrollments.objects.filter(student=self.request.user).order_by('class_enrolled')
        return context

class UserEnrollmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Enrollments
    success_url = reverse_lazy('Enrollment Record')

    def test_func(self):
        Enrollments = self.get_object()
        if self.request.user == Enrollments.student:
            return True
        return False

def logoutConfirmView(request):
    return render(request, 'users/logout-confirm.html')