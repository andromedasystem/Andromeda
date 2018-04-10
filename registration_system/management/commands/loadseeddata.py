from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from registration_system.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        # BUILINDG DATA: Currently Have 7 buildings COMPLETE
        # building_1 = Building.objects.create(name='Bill Gates Building', address='62 Scholar Lane')
        # building_2 = Building.objects.create(name='Ken Thompson Center', address='78 Lovelace Rd')
        # building_3 = Building.objects.create(name='Elon Musk Hall', address='82 Lovelace Rd')
        # building_4 = Building.objects.create(name='Alan Turing Center', address='12 Scholar Lane')
        # building_5 = Building.objects.create(name='Dennis Ritchie Hall', address='8 Lovelace Rd')
        # building_6 = Building.objects.create(name='Djisktra Labratory Center', address='21 Lovelace Rd')

        # ROOM DATA: Classroom, lab, lecture hall COMPLETE
        #   Currently have 2 classrooms CS106 and CS210
        # room_1 = Room.objects.create(building_id=building_1, type='Classroom',
        #                              capacity=30, room_number='CS106')
        # room = Room.objects.create(building_id=chosen_building, type=room_type,
        #                            capacity=room_capacity, room_number=room_number)
        # room_2 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=32, room_number='BG108')
        # room_3 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=25, room_number='BG110')
        # room_4 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=32, room_number='BG112')
        # room_5 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=32, room_number='BG114')
        # room_6 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Lecture Hall',
        #                              capacity=60, room_number='BG210')
        # room_7 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=28, room_number='BG212')
        # room_8 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                              capacity=32, room_number='BG214')
        # room_9 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Lecture Hall',
        #                              capacity=50, room_number='BG216')
        # room_10 = Room.objects.create(building_id=Building.objects.get(pk=1), type='LAB',
        #                               capacity=32, room_number='BG218')

        # room_11 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Classroom',
        #                               capacity=32, room_number='EM108')
        # room_12 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Classroom',
        #                               capacity=25, room_number='EM110')
        # room_13 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Classroom',
        #                               capacity=32, room_number='EM112')
        # room_14 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Classroom',
        #                               capacity=32, room_number='EM114')
        # room_15 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Lecture Hall',
        #                               capacity=60, room_number='EM210')
        # room_16 = Room.objects.create(building_id=Building.objects.get(pk=4), type='LAB',
        #                               capacity=28, room_number='EM212')
        # room_17 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Classroom',
        #                               capacity=32, room_number='EM214')
        # room_18 = Room.objects.create(building_id=Building.objects.get(pk=4), type='Lecture Hall',
        #                               capacity=50, room_number='EM216')
        # room_19 = Room.objects.create(building_id=Building.objects.get(pk=4), type='LAB',
        #                               capacity=32, room_number='EM218')
        # room_20 = Room.objects.create(building_id=Building.objects.get(pk=4), type='LAB',
        #                               capacity=32, room_number='EM220')
        #
        # room_21 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Classroom',
        #                               capacity=32, room_number='AT108')
        # room_22 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Classroom',
        #                               capacity=25, room_number='AT110')
        # room_23 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Classroom',
        #                               capacity=32, room_number='AT112')
        # room_24 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Classroom',
        #                               capacity=32, room_number='AT114')
        # room_25 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Lecture Hall',
        #                               capacity=60, room_number='AT210')
        # room_26 = Room.objects.create(building_id=Building.objects.get(pk=5), type='LAB',
        #                               capacity=28, room_number='AT212')
        # room_27 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Classroom',
        #                               capacity=32, room_number='AT214')
        # room_28 = Room.objects.create(building_id=Building.objects.get(pk=5), type='Lecture Hall',
        #                               capacity=50, room_number='AT216')
        # room_29 = Room.objects.create(building_id=Building.objects.get(pk=5), type='LAB',
        #                               capacity=32, room_number='AT218')
        # room_30 = Room.objects.create(building_id=Building.objects.get(pk=5), type='LAB',
        #                               capacity=32, room_number='AT220')
        #
        # room_31 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Classroom',
        #                               capacity=32, room_number='DR108')
        # room_32 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Classroom',
        #                               capacity=25, room_number='DR110')
        # room_33 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Classroom',
        #                               capacity=32, room_number='DR112')
        # room_34 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Classroom',
        #                               capacity=32, room_number='DR114')
        # room_35 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Lecture Hall',
        #                               capacity=60, room_number='DR210')
        # room_36 = Room.objects.create(building_id=Building.objects.get(pk=6), type='LAB',
        #                               capacity=28, room_number='DR212')
        # room_37 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Classroom',
        #                               capacity=32, room_number='DR214')
        # room_38 = Room.objects.create(building_id=Building.objects.get(pk=6), type='Lecture Hall',
        #                               capacity=50, room_number='DR216')
        # room_39 = Room.objects.create(building_id=Building.objects.get(pk=6), type='LAB',
        #                               capacity=32, room_number='DR218')
        # room_40 = Room.objects.create(building_id=Building.objects.get(pk=6), type='LAB',
        #                               capacity=32, room_number='DR220')
        #
        # room_41 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Classroom',
        #                               capacity=32, room_number='DL108')
        # room_42 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Classroom',
        #                               capacity=25, room_number='DL110')
        # room_43 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Classroom',
        #                               capacity=32, room_number='DL112')
        # room_44 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Classroom',
        #                               capacity=32, room_number='DL114')
        # room_45 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Lecture Hall',
        #                               capacity=60, room_number='DL210')
        # room_46 = Room.objects.create(building_id=Building.objects.get(pk=7), type='LAB',
        #                               capacity=28, room_number='DL212')
        # room_47 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Classroom',
        #                               capacity=32, room_number='DL214')
        # room_48 = Room.objects.create(building_id=Building.objects.get(pk=7), type='Lecture Hall',
        #                               capacity=50, room_number='DL216')
        # room_49 = Room.objects.create(building_id=Building.objects.get(pk=7), type='LAB',
        #                               capacity=32, room_number='DL218')
        # room_50 = Room.objects.create(building_id=Building.objects.get(pk=7), type='LAB',
        #                               capacity=32, room_number='DL220')
        #
        # room_61 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                               capacity=32, room_number='CS108')
        # room_62 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                               capacity=25, room_number='CS110')
        # room_63 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                               capacity=32, room_number='CS112')
        # room_64 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                               capacity=32, room_number='CS114')
        # room_65 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Lecture Hall',
        #                               capacity=60, room_number='CS210')
        # room_66 = Room.objects.create(building_id=Building.objects.get(pk=1), type='LAB',
        #                               capacity=28, room_number='CS212')
        # room_67 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Classroom',
        #                               capacity=32, room_number='CS214')
        # room_68 = Room.objects.create(building_id=Building.objects.get(pk=1), type='Lecture Hall',
        #                               capacity=50, room_number='CS216')
        # room_69 = Room.objects.create(building_id=Building.objects.get(pk=1), type='LAB',
        #                               capacity=32, room_number='CS218')
        # room_70 = Room.objects.create(building_id=Building.objects.get(pk=1), type='LAB',
        #                               capacity=32, room_number='CS220')

        # department_1 = Department.objects.create(name='History Department', phone_number='+15166829920',
        #                                          building_id=Building.objects.get(pk=2))
        # department_2 = Department.objects.create(name='Liberal Arts Department', phone_number='+15166828520',
        #                                          building_id=Building.objects.get(pk=2))
        # department_3 = Department.objects.create(name='Business Department', phone_number='+15164329920',
        #                                          building_id=Building.objects.get(pk=3))
        # department_4 = Department.objects.create(name='Biological Sciences Department', phone_number='+15162349920',
        #                                          building_id=Building.objects.get(pk=3))
        # department_5 = Department.objects.create(name='Chemistry Department', phone_number='+15169823900',
        #                                          building_id=Building.objects.get(pk=4))
        # department_6 = Department.objects.create(name='Physics Department', phone_number='+15169733200',
        #                                          building_id=Building.objects.get(pk=4))
        # department_7 = Department.objects.create(name='Criminology Department', phone_number='+15169888570',
        #                                          building_id=Building.objects.get(pk=5))
        # department_8 = Department.objects.create(name='English Department', phone_number='+15168750920',
        #                                          building_id=Building.objects.get(pk=5))
        # department_9 = Department.objects.create(name='Psychology Department', phone_number='+15162344400',
        #                                          building_id=Building.objects.get(pk=6))
        # department_10 = Department.objects.create(name='Sociology Department', phone_number='+15166822030',
        #                                           building_id=Building.objects.get(pk=6))
        # department_11 = Department.objects.create(name='Education Department', phone_number='+15162203450',
        #                                           building_id=Building.objects.get(pk=7))
        # department_12 = Department.objects.create(name='Music Department', phone_number='+15161200999',
        #                                           building_id=Building.objects.get(pk=7))
        # department_13 = Department.objects.create(name='History Department', phone_number='+15166829920',
        #                                          building_id=Building.objects.get(pk=1))

        # SEMESTER DATA : 2018 FALL SPRING WINTER SUMMER, 2017 F S W S, 2016 FALL SPRING, 2015 FALL SPRING
        # semester_1 = Semester.objects.create(year='2018', season='FALL')
        # semester_2 = Semester.objects.create(year='2018', season='WINTER')
        # semester_3 = Semester.objects.create(year='2018', season='SPRING')
        # semester_4 = Semester.objects.create(year='2018', season='SUMMER')
        # semester_5 = Semester.objects.create(year='2017', season='FALL')
        # semester_6 = Semester.objects.create(year='2017', season='WINTER')
        # semester_7 = Semester.objects.create(year='2017', season='SPRING')
        # semester_8 = Semester.objects.create(year='2017', season='SUMMER')
        # semester_9 = Semester.objects.create(year='2016', season='FALL')
        # semester_10 = Semester.objects.create(year='2016', season='SPRING')
        # semester_11 = Semester.objects.create(year='2015', season='FALL')
        # semester_12 = Semester.objects.create(year='2015', season='SPRING')

        # MEETING DAYS DATA:
        # days = MeetingDays.objects.create(day_1='Monday', day_2='Wednesday', day_3='Friday')
        # days = MeetingDays.objects.create(day_1='Tuesday', day_2='Thursday', day_3='Friday')
        # days = MeetingDays.objects.create(day_1='Tuesday', day_2='Thursday')
        # days = MeetingDays.objects.create(day_1='Saturday')
        # days = MeetingDays.objects.create(day_1='Sunday')