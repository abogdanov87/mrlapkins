from rest_framework import generics, permissions, status
from rest_framework_bulk import ListBulkCreateUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import glob, os
from django.conf import settings
import copy
from django.core.mail import send_mail 
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from django.db.models.functions import Lower
from django.utils import timezone
import datetime

from transliterate import translit


from common.models import (
    Param,
    User, 
)
from .serializers import (
    ParamSerializer,
    UserSerializer, 
)
from .filters import (
    ParamFilter,
)


class ParamRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer


class ParamListCreateAPIView(ListBulkCreateUpdateAPIView):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer
    filterset_class = ParamFilter

    def post(self, request, *args, **kwargs):
        reversed_specific_pre_processor_mapping = {
            u" ": u"_",
            u"%": u"percent",
        }
        code = translit(request.data['name'], 'ru', reversed=True).lower()
        request.data.update({
            'code': code
        })
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request_data = copy.copy(request.data)
        request.data.clear()
        new_request_data = []
        for data in request_data:
            code = translit(
                data['name'], 
                'ru', 
                reversed=True,
            ).replace(' ', '_').replace('%', 'percent').lower()
            data.update({
                'code': code
            })
            request.data.append(data)
        return self.bulk_update(request, *args, **kwargs)


class MeAPIView(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        me = request.user
        serializer = UserSerializer(me)
        return Response(serializer.data)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        generated_pwd = '00000{0}'.format(random.randint(0, 999999))[-6:]
        email = request.data['email']

        user_instance = None
        try:
            user_instance = User.objects.get(is_active=True, email__lower=email)
        except:
            user_instance = User(
                is_superuser=False,
                is_staff=False,
                is_active=True,
                username=email,
                email=email,
            )
        user_instance.user_instance = generated_pwd
        user_instance.password_change_date = datetime.datetime.now()
        user_instance.save()

        subject = 'Рады приветствовать вас на 4Paws!'
        html_message = render_to_string('registration_msg_russian.html', { 'registration_code': generated_pwd })
        plain_message = strip_tags(html_message)
        
        r = send_mail(
            subject = subject, 
            message = plain_message, 
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email],
            fail_silently = False,
            html_message = html_message,
        )
        
        return Response({
            'status': status.HTTP_200_OK,
        })
    