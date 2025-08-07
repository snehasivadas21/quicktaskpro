from django.shortcuts import render
from rest_framework import generics,viewsets,filters
from .models import User,Organization,Project,Task
from .serializers import UserRegisterSerializer,OrganizationSerializer,ProjectSerializer,TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsAdmin,IsManager,IsMember,IsInOrganization
from .signals import set_current_user

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=UserRegisterSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated,IsAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Organization.objects.filter(id=user.organization_id)
        return Organization.objects.none()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class =  ProjectSerializer
    permission_classes = [IsAuthenticated,IsAdmin]

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)
    def perform_create(self,serializer):
        serializer.save(organization=self.request.user.organization)  

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter] 
    search_fields = ['status','assigned_to__username']
    ordering_fields = ['due_date']

    def get_permissions(self):
        if self.request.method in ['POST','PUT','PATCH','DELETE']:
            return [IsAuthenticated(),IsManager()]
        return [IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        org_tasks=Task.objects.filter(organization=user.organization)      
        if user.role == 'member':
            return org_tasks.filter(assigned_to=user)
        return org_tasks
    
    def perform_create(self,serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user,
            updated_by=self.request.user
        )

    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user) 

    def initialize_request(self,request,*args,**kwargs):
        set_current_user(request.user)       
        return super().initialize_request(request,*args,**kwargs)
