from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import Building


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        print("CREATE BUILDING\n")
        name = input("Enter Building Name:")
        address = input("Enter Building Address:")
        building = Building.objects.create(name=name, address=address)
        print(building)