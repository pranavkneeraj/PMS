"""
This view module is used to specify the User Details
"""

from user.models import User, UniqueRegistration
from user.serializers import UserSerializer
from user.serializers import UserDetailSerializer
from user.serializers import UserBesicDataSerializer, UniqueRegistrationSerializer

from rest_framework import viewsets
from django.contrib.auth.views import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
import json
from rest_framework import status, views
from django.views.decorators.csrf import csrf_exempt
from user.tasks import send_mail
from django.http import HttpResponseRedirect
from rest_framework.parsers import FileUploadParser
class UserDetailViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    print("this is user detail top most")
    permission_classes = (AllowAny,)
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(deleted_on=None)

class UniqueRegistrationViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UniqueRegistrationSerializer
    queryset = UniqueRegistration.objects.filter(deleted_on=None)
class AddUsersAPI(views.APIView):
    # pylint: disable = too-many-ancestors
    """
    asdasdsad
    """
    #parser_classes = (FileUploadParser,)
    def post(self, request, format=None):
        """
        abc
        """
        total_added = 0
        total_modified = 0
        total_failed_to_add = 0

        #print("adadsd", help(request.data.get('file')))
        import xlrd
        if request.data.get('file', None):
            xlsfile = request.data.get('file').read()
            myexcel = xlrd.open_workbook(file_contents=xlsfile)
            print("WorkSheets:", myexcel.nsheets)
            sheet = myexcel.sheet_by_index(0)
            users = []
            for row_index in range(1,sheet.nrows):
                user = {}
                if(sheet.cell(row_index,0).value and sheet.cell(row_index,3).value):
                    #user['roll_no'] = ''
                    user['first_name'] = sheet.cell(row_index,0).value
                    user['middle_name'] = sheet.cell(row_index,1).value
                    user['last_name'] = sheet.cell(row_index,2).value
                    user['email'] = sheet.cell(row_index,3).value
                    user['is_active']=False
                    users.append(user)
                    print(user)
        else:
            users = request.data.get('user_list', [])
            print("users", users)
        email_list = []
        total_added = 0
        total_modified = 0
        total_failed_to_add = 0
        failed_students_data = []
        for user in users:
            print("user",user)
            serializer = UserBesicDataSerializer(data=user)
            if serializer.is_valid():
                print("valid", serializer.is_valid())
                serializer.save()
                email_list.append(serializer.data['email'])
                total_added+=1
            else:
                total_failed_to_add +=1
                user['reason']=serializer.errors
                failed_students_data.append(user)
                print(serializer.errors)
        # print(email_list)
        #send_mail(email_list)
        return Response({'total_added': total_added, 'total_faied_to_add':total_failed_to_add, 'failed_students_data':failed_students_data})

class AuthUserViewSet(APIView):

    """
    AuthUserViewSet
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['delete'], url_path='id')
    def delete(self, request):
        """
        this model delete will log the user out
        """
        # user = self.get_object(request.user)
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    print("in auth user model????????")

    def post(self, request):
        """
        this model will log the authenticated user in
        """
        print("in auth user...post method")
        email = request.data['email']
        print("adfsdfsa", request.data)
        password = request.data['password']
        account = authenticate(email=email, password=password)
        print(account)
        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = UserDetailSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'User Not active'
                },status=status.HTTP_403_FORBIDDEN)

        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'User not Authenticated'
            },status=status.HTTP_401_UNAUTHORIZED)

class RegistrationViewSet(APIView):

    """
    AuthUserViewSet
    """
    permission_classes = (AllowAny,)
    def get(self, request, uuid):
        """
        this model will log the authenticated user in
        """
        print("inside it")
        unique_code = UniqueRegistration.objects.get(code=uuid)
        if unique_code.user.is_active:
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/register/{}".format(uuid), {'user':unique_code.user})
class MeViewSet(APIView):
    """
    this model will show thw details of user logged in "
    """
    serializer_class = UserDetailSerializer
    def get(self, request, email):
        """
        this method will return logged in user details
        """
        account = User.objects.get(email=email)
        serializer = UserDetailSerializer(account)
        return Response(serializer.data)
