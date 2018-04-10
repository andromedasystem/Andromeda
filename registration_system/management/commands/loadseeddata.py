from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building, Room


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """

        # room = Room.objects.create(building_id=chosen_building, type=room_type,
        #                            capacity=room_capacity, room_number=room_number)
