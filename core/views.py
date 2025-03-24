from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, PYQ
from .serializers import CourseSerializer
from django.http import FileResponse
from django.conf import settings
import os

@api_view(['GET'])
def course_details(request):
    courses = Course.objects.prefetch_related('subjects').all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_pdf(request):
    pdf_link = request.data.get('pdf_link')

    if not pdf_link:
        return Response({"error": "No PDF link provided"}, status=400)

    pdf_filename = os.path.basename(pdf_link)  

    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', pdf_filename)

    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return Response({"error": "File not found"}, status=404)

@api_view(['GET'])
def course_pyqs(request):
    courses = Course.objects.all()
    response_data = {}

    for course in courses:
        pyqs = PYQ.objects.filter(course=course)
        file_paths = [pyq.file.url for pyq in pyqs]
        response_data[course.title] = file_paths
    return Response(response_data)

@api_view(['POST'])
def get_pyq(request):
    relative_path = request.data.get('pdf_link') 

    if not relative_path:
        return Response({"error": "No PDF link provided"}, status=400)

    file_path = os.path.join(settings.MEDIA_ROOT, relative_path.lstrip("/media/"))

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return Response({"error": "File not found"}, status=404)
