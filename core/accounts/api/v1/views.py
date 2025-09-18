from rest_framework.views import APIView
from accounts.api.v1.permissions import IsManager
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import BusinessWorker, AccessTokenBlackList
from accounts.api.v1.serializers import (
    WorkingTimeSerializer,
    WorkerSerializer,
    ManagerSerializer,
    LogoutSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError

User = get_user_model()


class UserProfileView(APIView):

    def get(self, request):
        """
        Retrieve the profile of a user.
        """
        user = request.user
        if hasattr(user, "business_workers"):
            serializer = WorkerSerializer(user.business_workers)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif hasattr(user, "business_manager"):
            serializer = ManagerSerializer(user.business_manager)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(
            data={"detail": "Bad request"}, status=status.HTTP_400_BAD_REQUEST
        )


class UserLogoutView(APIView):
    def post(self, request):
        """
        Logout user and invalidate refresh and access tokens.
        """
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token_str = serializer.validated_data["refresh_token"]
        access_token_str = serializer.validated_data["access_token"]

        try:
            # Invalidate refresh token
            refresh_token = RefreshToken(refresh_token_str)
            refresh_token.blacklist()

            # Blacklist access token derived from refresh
            derived_access_token = refresh_token.access_token
            derived_access_token_str = str(derived_access_token)
            AccessTokenBlackList.objects.get_or_create(
                token=derived_access_token_str
            )

            # Invalidate access token
            access_token = AccessToken(access_token_str)
            access_token_str = str(access_token)

            AccessTokenBlackList.objects.get_or_create(
                token=access_token_str
            )

        except TokenError as error:
            return Response(
                {"detail": str(error)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as error:
            return Response(
                {"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserUpdateView(APIView):
    permission_classes = [IsManager]

    def post(self, request, user_slug):
        """
        Update the working time of a worker.
        Only accessible by managers.
        """
        business_worker = get_object_or_404(
            BusinessWorker,
            user__user_slug=user_slug
        )
        serializer = WorkingTimeSerializer(
            data=request.data,
            context={
                "request": request,
                "worker": business_worker
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(business_worker=business_worker)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
