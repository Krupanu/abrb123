from django.urls import path
from .views import DynamicFormView, FormSubmitView, DataListView

urlpatterns = [
    path('', DynamicFormView.as_view(), name='form'),
    path('submit/', FormSubmitView.as_view(), name='submit'),
    path('list/', DataListView.as_view(), name='list'),
]