from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    full_company_name = models.CharField(max_length=100)
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CompanyUser(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ci = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ci = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
