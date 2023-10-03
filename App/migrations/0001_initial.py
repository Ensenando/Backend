# Generated by Django 4.2.4 on 2023-10-03 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('num_by_lesson', models.IntegerField(default=1)),
                ('kind', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('url', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('names', models.CharField(max_length=100)),
                ('surnames', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('nationality', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Profesor', 'Profesor'), ('Estudiante', 'Estudiante'), ('Admin', 'Admin')], max_length=20)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('student', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('lesson', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.lesson')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TheoryActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
            ],
        ),
        migrations.CreateModel(
            name='SecuenceActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageReference', models.CharField(blank=True, max_length=500, null=True)),
                ('image1', models.CharField(blank=True, max_length=500, null=True)),
                ('image2', models.CharField(blank=True, max_length=500, null=True)),
                ('image3', models.CharField(blank=True, max_length=500, null=True)),
                ('image4', models.CharField(blank=True, max_length=500, null=True)),
                ('image5', models.CharField(blank=True, max_length=500, null=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecognitionActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning', models.CharField(blank=True, max_length=500, null=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('notification', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.notification')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='userStudent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationUserStudent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='userTutor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificationUserTutor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MemoryActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.CharField(blank=True, max_length=500, null=True)),
                ('image2', models.CharField(blank=True, max_length=500, null=True)),
                ('image3', models.CharField(blank=True, max_length=500, null=True)),
                ('image4', models.CharField(blank=True, max_length=500, null=True)),
                ('image5', models.CharField(blank=True, max_length=500, null=True)),
                ('pairimage1', models.CharField(blank=True, max_length=500, null=True)),
                ('pairimage2', models.CharField(blank=True, max_length=500, null=True)),
                ('pairimage3', models.CharField(blank=True, max_length=500, null=True)),
                ('pairimage4', models.CharField(blank=True, max_length=500, null=True)),
                ('pairimage5', models.CharField(blank=True, max_length=500, null=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('lessonUser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.userlesson')),
            ],
        ),
        migrations.CreateModel(
            name='LinkActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.CharField(blank=True, max_length=500, null=True)),
                ('image2', models.CharField(blank=True, max_length=500, null=True)),
                ('image3', models.CharField(blank=True, max_length=500, null=True)),
                ('image4', models.CharField(blank=True, max_length=500, null=True)),
                ('image5', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning1', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning2', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning3', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning4', models.CharField(blank=True, max_length=500, null=True)),
                ('meaning5', models.CharField(blank=True, max_length=500, null=True)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.activity')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('userStudent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='goalUserStudent', to=settings.AUTH_USER_MODEL)),
                ('userTutor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='goalUserTutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.lesson')),
                ('userStudent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificateUserStudent', to=settings.AUTH_USER_MODEL)),
                ('userTutor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificateUserTutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='lesson',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.lesson'),
        ),
    ]
