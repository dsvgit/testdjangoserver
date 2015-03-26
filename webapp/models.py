from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

class User(models.Model):
	login = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	passwd = models.CharField(max_length=30)
	org = models.ForeignKey(Organization)
	def __str__(self):
		return self.login

class Purchase(models.Model):
	name = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True, blank=True)
	user = models.ForeignKey(User)
	cost = models.FloatField()
	def __str__(self):
		return self.name