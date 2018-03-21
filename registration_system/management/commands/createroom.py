from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building, Room


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE ROOM\n")
        room_number = input("Enter Room Number (e.g. CS280) :")
        room_type = input("Enter Room Type:")
        room_capacity = input("Enter Capacity")
        print("\n")
        building = Building.objects.all().order_by('building_id')
        for b in building:
            print(b)
        building_number = input("Please Choose One of the building's ID's above as the Department's Building")
        chosen_building = Building.objects.get(pk=int(building_number))
        room = Room.objects.create(building_id=chosen_building, type=room_type,
                                   capacity=room_capacity, room_number=room_number)
        print(room)
