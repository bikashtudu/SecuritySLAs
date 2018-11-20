from django import forms

VM_CHOICES = (
	('vm1','VM1'),
	('vm2','VM2'),
	('vm3','VM3')
	)

SLA_TYPE_CHOICES = (
	('UserAccess','User Access'),
	('ServiceAvailablity','Service Availablity'),
	('UserLogin','User Login'),
	('SoftwareIntegrity','Software Integrity')
	)

STATUS_CHOICES = (
	('Complied','Complied'),
	('Error','Error'),
	('Uncomplied','Uncomplied')
	)

class SLAQueryForm(forms.Form):
	VM = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=VM_CHOICES)
	SLAType = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=SLA_TYPE_CHOICES)
	Status = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=STATUS_CHOICES)
	StartTimeStamp = forms.DateTimeField()
	EndTimeStamp = forms.DateTimeField()
	
	def clean(self):
		cleaned_data = super(SLAQueryForm, self).clean()
		VM = cleaned_data.get('VM')
		SLAType = cleaned_data.get('SLAType')
		Status = cleaned_data.get('Status')
		StartTimeStamp = cleaned_data.get('StartTimeStamp')
		EndTimeStamp = cleaned_data.get('EndTimeStamp')
		
		if not StartTimeStamp:
			raise forms.ValidationError('Start TimeStamp is needed')
		else:
			if EndTimeStamp:
				if StartTimeStamp > EndTimeStamp:
					raise forms.ValidationError('End TimeStamp is less than Start Time Stamp')

