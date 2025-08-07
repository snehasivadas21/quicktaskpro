from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Organization(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('manager','Manager'),
        ('member','Member'),
    )    
    role=models.CharField(max_length=50,choices=ROLE_CHOICES)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='users')

    def __str__(self):
        return f"{self.role}"
    
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo','ToDo'),
        ('inprogress','In Progress'),
        ('done','Done'),
    )  
    title = models.CharField(max_length=200)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='todo')
    due_date=models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_tasks')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
