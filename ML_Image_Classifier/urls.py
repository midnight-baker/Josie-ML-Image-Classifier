"""
Definition of urls for ML_Image_Classifier.
"""

from datetime import datetime
from django.urls import path
from app import forms, views

urlpatterns = [
    path('', views.try_josie, name='try_josie'),
    path('about_creator/', views.about_creator, name='about_creator'),
    path('about_josie/', views.about_josie, name='about_josie'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
