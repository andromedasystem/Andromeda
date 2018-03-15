from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from django.contrib.auth.models import User
from registration_system.models import Student, FullTimeStudent, PartTimeStudent, UserProfile
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE STUDENT USER\n")
        first_name = input("Enter Users First Name:")
        last_name = input("Enter Users Last Name:")
        username = input("Enter Username:")
        password = input("Enter Password:")
        email = input("Enter Email Address:")
        # TODO:
        date_entry = input("Enter Date in YYYY-MM-DD format:")
        year, month, day = map(int, date_entry.split('-'))
        date_input = datetime.date(year, month, day)
        student_type = input("Enter the letter 'F' to createa full-time student or 'P' to create a part-time student.")
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password, email=email)
        profile = user.userprofile
        profile.user_type = 'S'
        profile.save()
        student = Student.objects.create(student_id=profile, date_of_birth=date_input,
                                         student_type=student_type.strip())
