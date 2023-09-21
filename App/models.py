from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from enum import Enum

class Role(Enum):
    PROFESOR = 'Profesor'
    ESTUDIANTE = 'Estudiante'
    ADMIN = 'Admin'

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        if not email: # If email is not provided 
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields) # Normalize email
        user.set_password(password) # Set password
        user.save(using=self._db) # Save user


        return user
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.role = Role.ADMIN.value
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) # ._db meaning the database that is being used
  
        return user

class User(AbstractBaseUser, PermissionsMixin):
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=[(role.value, role.value) for role in Role])
    student = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,default='')
    objects = UserManager()

    USERNAME_FIELD = 'email' # This is the field that will be used to login

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)

class Score(models.Model):
    score = models.IntegerField()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class Goal(models.Model):
    objective = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class Resource(models.Model):
    kind = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=500, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)

class Certificate(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)

class Dictionary(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=300)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    design = models.CharField(max_length=100)

class Notification(models.Model):
    kind = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)