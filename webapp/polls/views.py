from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SLAStatus
from django.contrib.auth.models import User
from .filters import SLAResultFilter
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

