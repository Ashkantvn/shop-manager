from rest_framework.views import APIView
from accounts.api.v1.permissions import IsManager
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import BusinessWorker
from accounts.api.v1.serializers import WorkingTimeSerializer, WorkerSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileView(APIView):

    def get(self, request):
        """
        Retrieve the profile of a user.
        """
        user  = request.user
        serializer = WorkerSerializer(user.business_workers)
        if hasattr(user, 'business_workers'):
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'detail': serializer.data}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    pass
    
class UserLogoutView(APIView):
    pass
    
class UserUpdateView(APIView):
    permission_classes = [IsManager]
    
    def post(self, request, username):
        """
        Update the working time of a worker.
        Only accessible by managers.
        """
        business_worker = get_object_or_404(BusinessWorker, user__username=username)
        serializer = WorkingTimeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(business_worker=business_worker)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)