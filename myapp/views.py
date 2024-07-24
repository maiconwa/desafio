import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.parsers import MultiPartParser

# Create your views here.

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, World!'})


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request, format=None):
        file_obj = request.FILES['file']
        #print(file_obj.file)
        fileContent = "None"
        while fileContent:
            # reading contents of the file
            fileContent = file_obj.readline()
            fileContent = fileContent.strip()
            # printing the contents of the file
            print(fileContent)
        # closing the file
        file_obj.close()
        # Process the file here
        return Response({'message': 'File uploaded successfully'})