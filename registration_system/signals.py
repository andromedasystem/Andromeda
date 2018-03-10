from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Admin, Researcher, Student, Faculty, \
    FullTimeStudent, PartTimeStudent, FullTimeFaculty, PartTimeFaculty


@receiver(post_save, sender=User)
def create_admin(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'user_type'):
            if instance.user_type == 'A':
                Admin.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_researcher(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'user_type'):
            if instance.user_type == 'R':
                Researcher.objects.create(user=instance)


@receiver(post_save, sender=Student)
def create_full_time_student(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'student_type'):
            if instance.student_type == 'F':
                FullTimeStudent.objects.create(student_id=instance)


@receiver(post_save, sender=Student)
def create_part_time_student(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'student_type'):
            if instance.student_type == 'P':
                PartTimeStudent.objects.create(student_id=instance)


@receiver(post_save, sender=Faculty)
def create_part_time_faculty(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'faculty_type'):
            if instance.faculty_type == 'F':
                PartTimeFaculty.objects.create(faculty_id=instance)


@receiver(post_save, sender=Faculty)
def create_full_time_faculty(sender, instance ,created, **kwargs):
    if created:
        if hasattr(instance, 'faculty_type'):
            if instance.faculty_type == 'P':
                FullTimeFaculty.objects.create(faculty_id=instance)
