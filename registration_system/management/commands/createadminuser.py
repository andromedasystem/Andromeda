from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from django.contrib.auth.models import User
from registration_system.models import Admin, UserProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE ADMIN USER\n")
        first_name = input("Enter Users First Name:")
        last_name = input("Enter Users Last Name:")
        username = input("Enter Username:")
        password = input("Enter Password:")
        email = input("Enter Email Address:")
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password, email=email)
        profile = user.userprofile
        profile.user_type = 'A'
        profile.save()
        admin = Admin.objects.create(admin_id=profile)
        print(user)