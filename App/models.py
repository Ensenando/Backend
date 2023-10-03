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
    username = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email' # This is the field that will be used to login

class UserAudit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    log_date = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500, blank=True, null=True)

class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    num_by_lesson = models.IntegerField(default=1)
    kind = models.CharField(max_length=100, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)

class TheoryActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    meaning = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class LinkActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    image1 = models.CharField(max_length=500, blank=True, null=True)
    image2 = models.CharField(max_length=500, blank=True, null=True)
    image3 = models.CharField(max_length=500, blank=True, null=True)
    image4 = models.CharField(max_length=500, blank=True, null=True)
    image5 = models.CharField(max_length=500, blank=True, null=True)
    meaning1 = models.CharField(max_length=500, blank=True, null=True)
    meaning2 = models.CharField(max_length=500, blank=True, null=True)
    meaning3 = models.CharField(max_length=500, blank=True, null=True)
    meaning4 = models.CharField(max_length=500, blank=True, null=True)
    meaning5 = models.CharField(max_length=500, blank=True, null=True)

class MemoryActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    image1 = models.CharField(max_length=500, blank=True, null=True)
    image2 = models.CharField(max_length=500, blank=True, null=True)
    image3 = models.CharField(max_length=500, blank=True, null=True)
    image4 = models.CharField(max_length=500, blank=True, null=True)
    image5 = models.CharField(max_length=500, blank=True, null=True)
    pairimage1 = models.CharField(max_length=500, blank=True, null=True)
    pairimage2 = models.CharField(max_length=500, blank=True, null=True)
    pairimage3 = models.CharField(max_length=500, blank=True, null=True)
    pairimage4 = models.CharField(max_length=500, blank=True, null=True)
    pairimage5 = models.CharField(max_length=500, blank=True, null=True)

class SecuenceActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    imageReference = models.CharField(max_length=500, blank=True, null=True) 
    image1 = models.CharField(max_length=500, blank=True, null=True)
    image2 = models.CharField(max_length=500, blank=True, null=True)
    image3 = models.CharField(max_length=500, blank=True, null=True)
    image4 = models.CharField(max_length=500, blank=True, null=True)
    image5 = models.CharField(max_length=500, blank=True, null=True)

class RecognitionActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    meaning = models.CharField(max_length=500, blank=True, null=True)

class Score(models.Model):
    score = models.IntegerField()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class Goal(models.Model):
    objective = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    userTutor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='goalUserTutor')
    userStudent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='goalUserStudent')

class Medal(models.Model):
    lessonUser = models.ForeignKey(UserLesson, on_delete=models.CASCADE, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class Certificate(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    userTutor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='certificateUserTutor')
    userStudent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='certificateUserStudent')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)

class Tutorial(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=1000, blank=True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True)

class Notification(models.Model):
    kind = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    userTutor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='notificationUserTutor')
    userStudent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='notificationUserStudent')

class NotificationUser(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True)

