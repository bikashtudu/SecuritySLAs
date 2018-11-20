from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SLAStatus
from django.contrib.auth.models import User
from .filters import SLAResultFilter
from .forms import SLAQueryForm
from .SLAReq import SLAResult
# Create your views here.

@login_required(login_url='/login/')
def index(request):
	SLAOutput = SLAStatus.objects.filter(username=request.user)
	SLAFilter = SLAResultFilter(request.GET,queryset=SLAOutput)
	HasFilters = any(field in request.GET for field in set(SLAFilter.get_fields()))
	context={
		'title':'Home',
		'filter':SLAFilter,
		'hasfilter':HasFilters,
	}
	return render(request,'polls/index.html',context)


def about(request):
	context={
		'title':'About'
	}
	return render(request,'polls/about.html',context)

@login_required(login_url='/login/')
def SLAQuery(request):
	if request.method == 'POST':
		form = SLAQueryForm(request.POST)
		isQuery=1
		# form.clean()
		if form.is_valid():
			SLAQueryResult = []
			for currvm in form.cleaned_data['VM']:
				for currSLA in form.cleaned_data['SLAType']:
					SLAQueryResult.append(SLAResult(currvm,currSLA,'Complied'))
			context = {
			'title':'SLA Query',
			'form':form,
			'isQuery':isQuery,
			'StartTimeStamp':form.cleaned_data['StartTimeStamp'],
			'EndTimeStamp':form.cleaned_data['EndTimeStamp'],
			'VM':form.cleaned_data['VM'],
			'SLAType':form.cleaned_data['SLAType'],
			'Status':form.cleaned_data['Status'],
			'SLAQueryResult':SLAQueryResult,
			}
		else:
			context = {
			'title':'SLA Query',
			'form':form,
			'isQuery':isQuery,
			'isError':1,
			}
		return render(request,'polls/SLAQuery.html',context)
	else:
		form = SLAQueryForm()
	context = {
		'title':'SLA Query',
		'form':form,
	}
	return render(request,'polls/SLAQuery.html',context)
