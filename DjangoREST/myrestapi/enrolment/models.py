from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
#from django.utils.timezone import now
from django.urls import reverse
 
class Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )
 
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    highest_grade=models.TextField(max_length=20,  null=True)
    matric_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    matric_certificate = models.ImageField(upload_to="images", null=True)

    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="")
 
    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('users')
 