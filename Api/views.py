from django.http import JsonResponse
from .models import SignupCourses
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string


@api_view(['GET', 'POST'])
def home_api(request):
    if request.method == 'GET':
        courses = SignupCourses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse({"Courses" : serializer.data})
    
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #headers = get_success_headers(serializer.data)
            return Response({"Courses" : serializer.data, 'status':status.HTTP_201_CREATED})
        
        return Response({'status':status.HTTP_400_BAD_REQUEST})
        
        
@api_view(['GET', 'POST'])        
def contactform(request):
    if request.method == 'POST':
        data=request.data
        print(data)
        
        name = data['name']
        email = data['email']
        content = data['message']
        
        html = render_to_string('emails/email.html', {
            'name' : name,
            'email' : email,
            'content' : content
        })
        
        send_mail("the sub", "the mess", "viczik16@gmail.com", ["victor_zik@yahoo.com"], html_message=html)
        
        return Response({'status':status.HTTP_400_BAD_REQUEST})