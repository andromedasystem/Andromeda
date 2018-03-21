from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building, MeetingDays


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE MEETING DAYS\n")
        day_1 = input("Enter Day 1 :")
        day_2 = input("Enter Day 2 : (Type N if not applicable)")
        day_3 = input("Enter Day 3 : (Type N if not applicable)")
        if day_2 != 'N':
            if day_3 != 'N':
                days = MeetingDays.objects.create(day_1=day_1, day_2=day_2, day_3=day_3)
            else:
                days = MeetingDays.objects.create(day_1=day_1, day_2=day_2)
        else:
            days = MeetingDays.objects.create(day_1=day_1)

        print(days)
