from rest_framework import serializers
from .models import User,Organization,Project,Task
from django.contrib.auth.password_validation import validate_password

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id','name']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators=[validate_password])
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = User
        fields = ['id','username','email','password','role','organization']

    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            organization=validated_data['organization']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name','description']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'due_date',
            'assigned_to', 'project', 'created_by', 'updated_by',
            'created_at', 'updated_at'
        ]







