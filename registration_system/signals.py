from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Admin, Researcher, Student, Faculty, \
    FullTimeStudent, PartTimeStudent, FullTimeFaculty, PartTimeFaculty


@receiver(post_save, sender=User, dispatch_uid="user_post_create")
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User, dispatch_uid="user_post_save")
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()


# @receiver(post_save, sender=User, dispatch_uid="admin_post_create")
# def create_admin(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         if instance.userprofile:
#             if instance.userprofile.user_type == 'A':
#                 Admin.objects.create(admin_id=instance.userprofile)
#                 instance.userprofile.admin.save()
#
#
# @receiver(post_save, sender=User, dispatch_uid="researcher_post_create")
# def create_researcher(sender, instance, created, **kwargs):
#     if created:
#         if instance.userprofile:
#             if instance.userprofile.user_type == 'R':
#                 Researcher.objects.create(researcher_id=instance.userprofile)
#                 instance.userprofile.researcher.save()


@receiver(post_save, sender=Student, dispatch_uid="full_time_student_post_create")
def create_full_time_student(sender, instance, created, **kwargs):
    if created:
        if instance.student_type == 'F':
            FullTimeStudent.objects.create(student_id=instance)
            instance.fulltimestudent.save()


@receiver(post_save, sender=Student, dispatch_uid="part_time_student_post_create")
def create_part_time_student(sender, instance, created, **kwargs):
    if created:
        if instance.student_type == 'P':
            PartTimeStudent.objects.create(student_id=instance)
            instance.parttimestudent.save()


@receiver(post_save, sender=Faculty, dispatch_uid="full_time_faculty_post_create")
def create_full_time_faculty(sender, instance, created, **kwargs):
    if created:
        if instance.faculty_type == 'F':
            FullTimeFaculty.objects.create(faculty_id=instance)
            instance.fulltimefaculty.save()


@receiver(post_save, sender=Faculty, dispatch_uid="part_time_faculty_post_create")
def create_part_time_faculty(sender, instance, created, **kwargs):
    if created:
        if instance.faculty_type == 'P':
            PartTimeFaculty.objects.create(faculty_id=instance)
            instance.parttimefaculty.save()



