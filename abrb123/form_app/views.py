from django.shortcuts import render, redirect
from django.views import View
from .models import FormSubmission


class DynamicFormView(View):
    def get(self, request):
        return render(request, 'formapp/form.html')


class FormSubmitView(View):
    def post(self, request):
        names = []
        for key, value in request.POST.items():
            if key.startswith('name') and value and key != 'csrfmiddlewaretoken':
                names.append(value)
        
        if names:
            FormSubmission.objects.create(data={'names': names})
        
        return redirect('list')


class DataListView(View):
    def get(self, request):
        submissions = FormSubmission.objects.all()
        return render(request, 'formapp/list.html', {'submissions': submissions})