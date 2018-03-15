from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building, Department


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE DEPARTMENT\n")
        name = input("Enter Department Name:")
        phone_number_input = input("Enter 7 digit phone number with no dashes ####### :")
        phone_number = "+1516%s" % phone_number_input
        print("\n")
        building = Building.objects.all().order_by('building_id')
        for b in building:
            print(b)
        building_number = input("Please Choose One of the building's ID's above as the Department's Building")
        chosen_building = Building.objects.get(pk=int(building_number))
        department = Department.objects.create(name=name, phone_number=phone_number, building_id=chosen_building)
        print(department)