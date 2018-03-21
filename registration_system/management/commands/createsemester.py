from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building, Semester


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE SEMESTER\n")
        year = input("Enter Year :")
        season = input("Enter Season (choose WINTER, SPRING, FALL, or SUMMER")
        semester = Semester.objects.create(year=year, season=season)
        print(semester)
