from django.db import models
from django.contrib.auth.models import User

class VMs(models.Model):
	vm = models.CharField(max_length=10)
	
	def __str__(shelf):
		return shelf.vm

class UserVMs(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	vm = models.ForeignKey(VMs,on_delete=models.CASCADE)

class SLAStatus(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	vm = models.ForeignKey(VMs,on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	sla = models.CharField(max_length=40)
	status  = models.CharField(max_length=20)
