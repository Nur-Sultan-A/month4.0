from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):

    QUALIFICATION = (
        ('junior', 'junior'),
        ('senior', 'senior'),
        ('middle', 'middle'),
    )

    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )

    IT_LANGUAGES = (
        ('python', 'python'),
        ('java', 'java'),
        ('ruby', 'ruby'),
    )

    LANGUAGES = (
        ('English', 'English'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Russian', 'Russian'),
    )

    phone_number = models.CharField(max_length=13, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    it_languages = models.CharField(max_length=100, choices=IT_LANGUAGES, null=True, blank=True)
    languages = models.CharField(max_length=100, choices=LANGUAGES, null=True, blank=True)
    qualification = models.CharField(max_length=100, choices=QUALIFICATION, null=True, blank=True)


    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)


class EmailVerificationToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"Email verification for {self.user.email}"