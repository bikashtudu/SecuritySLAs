
from django import forms
from .models import SLAStatus,VMs
import django_filters

class SLAResultFilter(django_filters.FilterSet):
	vm = django_filters.ModelMultipleChoiceFilter(queryset=VMs.objects.all(),widget=forms.CheckboxSelectMultiple)
	timestamp = django_filters.DateTimeFromToRangeFilter()
	class Meta:
		model = SLAStatus
		fields = ['vm','sla','status',]
