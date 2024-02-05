from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Classes, Enrollments
from datetime import date
from .forms import EnrollmentForm
from django.contrib import messages

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollments
    fields = ['class_enrolled']
    success_url = reverse_lazy('Enrollment Record')

    #Classes.objects.filter(start_date__gte=date.today()).update(is_active=True)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['class_enrolled'].queryset = Classes.objects.filter(age_group=self.request.user.age).filter(is_active=True)
        return form

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

'''
def EnrollmentFilterForm(request):
    form = EnrollmentForm()
    return render(request, 'classes/enrollment.html', {'e_form': form})


def class_list(request):
    selected_date = request.GET.get('class_date')
    #classes = []
    if selected_date:
        classes = Classes.objects.filter(start_date=selected_date).filter(age_group=request.user.age)
        if classes:
            form = EnrollmentForm()
            form.fields['class_enrolled'].queryset = classes
            context = {
                'classes': classes,
                'form': form
            }
        return render(request, 'classes/enrollment.html', context)
    return render(request, 'classes/enrollment.html')


def class_list2(request):
    if request.method == 'POST':
        print('Hello World')
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class has been enrolled successfully!')
            return redirect('Enrollment Record')
        else:
            form = EnrollmentForm()
    return render(request, 'classes/enrollment.html', {'form': form})
'''