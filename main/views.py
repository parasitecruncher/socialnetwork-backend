from django.shortcuts import render
from api.serializers import ProfileSerializer,UserSerializer,ImageSerializer,LikeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status,generics
from rest_framework.views import APIView
from main.models import Profile,UserImages,Like
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import detail_route, list_route

import json
from rest_framework import viewsets, filters
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class Profile_List(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    parser_classes = (FileUploadParser,)
    def get(self, request, format=None):
        profiles=Profile.objects.all()
        serializer=ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        req=request.data
        image = req['display_image']
        req['user']=self.request.user.id
        #self.request.user.
        serializer=ProfileSerializer(data=req)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
# class Feed(APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#     def get(self,request,format=None):
#         queryset=self.request.user.Profile.friends.all().filter(friends=21);
#         print querXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXyset
#
#         return HttpResponse(queryset.query)

class Feed(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    #UserImages.objects.all().filter(pk__in=[9,10]).all()

    def post(self, request, format=None):
        from django.db.models import Q

        print list(User.objects.get(pk=self.request.user.id).profile.friends.all().values_list('userimages'))
        return Response(json.dumps(list(User.objects.get(pk=self.request.user.id).profile.friends.all().filter(~Q(userimages=None)).values('userimages__id','userimages__image','nick_name'))))
class Search(APIView):
    permissions= (permissions.AllowAny)
    def get(self,request,format=None):
        from django.db.models import Q
        st=request.query_params['search']
        print str(st)
        profiles = Profile.objects.all().filter(nick_name__istartswith=str(st))
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
        return JSONResponse(json.dumps(list(Profile.objects.all().filter(Q(nick_name__startswith=str(st))).values('id','nick_name'))))
class UserFeed(APIView):
    def post(self, request,pk, format=None):
        return Response(json.dumps(list(Profile.objects.all().filter(pk=pk).all().values('userimages__image','userimages__id'))))

    def get(self, request,pk, format=None):
        return Response(json.dumps(list(Profile.objects.all().filter(pk=pk).all().values('userimages__image','userimages__id'))))

class ImagesDetail(APIView):
    parser_classes = (FileUploadParser,)
    def get_object(self,pk):
        try:
            return UserImages.objects.get(pk=pk)
        #profile=Profile.objects.all()[0]

        except UserImages.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):
        image=self.get_object(pk=pk)
        serializer=ImageSerializer(image)
        return Response(serializer.data)

class ImagesAll(APIView):
    parser_classes = (FileUploadParser,)

    def get(self, request, format=None):
        image=UserImages.objects.all()
        serializer=ImageSerializer(image,many=True)
        return Response(serializer.data)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        return Response(status=204)
    def post(self, request, format=None):
        req=request.data
        req['user']=self.request.user.id
        #self.request.user.
        serializer=ImageSerializer(data=req)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)


class MyFriends(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        print  self.request.user.Profile.friends.all()#.filter(self.request.user.id)
        return  self.request.user.Profile.friends.all()#.filter(self.request.user.id)
    serializer_class = ProfileSerializer
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.request.user.Profile.friends.all().filter(request.user.id);
    #     serializer = ProfileSerializer(queryset, many=True)
    #     return Response(serializer.data)


#        return HttpResponse(queryset.query)
# class Profile_List(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user,user=self.request.user)
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
class Like_List(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



class User_List(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        #data=JSONParser().parse(request)
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None):
        data=JSONParser().parse(request)
        username=data['username']
        password=data['password']
        from django.contrib.auth import authenticate
        from rest_framework.authtoken.models import Token
        user = authenticate(username=username,password=password)
        if user is not None:
            return HttpResponse(Token.generate_key(user))
        else:
            return HttpResponse("Invalid!")


class ImagesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = UserImages.objects.all()
    serializer_class = ImageSerializer
    def perform_create(self, serializer):
        if serializer.is_valid():
            print serializer
            serializer.save(owner=self.request.user)


class Profile_Detail(APIView):
    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        #profile=Profile.objects.all()[0]

        except Profile.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):
        profile=self.get_object(pk)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #data= JSONParser().parse(request)
        profile=self.get_object(pk)
        req = request.data
        req['user'] = self.request.user.id
        # self.request.user.

        serializer=ProfileSerializer(profile,data=req)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class Profile_Detail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class User_Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer
#
# class User_Detail(APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
#     def get_object(self,pk):
#         try:
#             return User.objects.get(pk=pk)
#         #profile=Profile.objects.all()[0]
#
#         except Profile.DoesNotExist:
#             raise Http404
#
#     def get(self, request,pk, format=None):
#         user=self.get_object(pk)
#         serializer=UserSerializer(user)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         data=JSONParser().parse(request)
#         user=self.get_object(pk)
#         serializer=UserSerializer(user,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user=self.get_object(self,pk=pk)
#
#         user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#
# Create your views hee.

