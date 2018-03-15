from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from django.contrib.auth.models import User
from registration_system.models import Faculty, Department


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE FacultyT\n")
        first_name = input("Enter Users First Name:")
        last_name = input("Enter Users Last Name:")
        username = input("Enter Username:")
        password = input("Enter Password:")
        email = input("Enter Email Address:")
        faculty_type = input("Enter the letter 'F' to create a full-time faculty or 'P' to create a part-time faculty.")
        print("\n")
        department = Department.objects.all().order_by('department_id')
        for d in department:
            print(d)
        department_number = input("Please Choose One of the building's ID's above as the Department's Building")
        chosen_department = Department.objects.get(pk=int(department_number))
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password, email=email)

        profile = user.userprofile
        profile.user_type = 'F'
        profile.save()
        faculty = Faculty.objects.create(faculty_id=profile, department_id=chosen_department, faculty_type=faculty_type.strip())
        print(faculty)
