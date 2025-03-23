from core.views import course_details, get_pdf, course_pyqs
from django.urls import path

urlpatterns = [
    path('course_details/', course_details),
    path('get_pdf/', get_pdf),
    path('course_pyqs/', course_pyqs),
]
