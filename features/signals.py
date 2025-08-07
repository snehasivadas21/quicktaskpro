from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task
from threading import local

_user = local()

def set_current_user(user):
    _user.value=user

def get_current_user():
    return getattr(_user,'value',None)

@receiver(pre_save,sender=Task)
def add_audit_log(sender,instance,**kwargs):
    user = get_current_user()
    if user :
        if not instance.pk:
            instance.created_by = user
        instance.updated_by = user
                