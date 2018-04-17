from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from django.contrib.auth.models import User
from registration_system.models import Major, Minor, MinorRequirement, MajorRequirement


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command used to craete admin user

        :param args: not used
        :param options: not used
        """
        # major_1 = Major.objects.create(department_id_id=6, name="Accounting, B.S.")
        major_2 = Major.objects.create(department_id_id=14, name="Education: Mathematics B.S.")
        major_3 = Major.objects.create(department_id_id=8, name="Biochemistry, B.S.")
        major_4 = Major.objects.create(department_id_id=7, name="Biological Sciences, B.S.")
        major_5 = Major.objects.create(department_id_id=6, name="Business Administration, B.S.")
        major_6 = Major.objects.create(department_id_id=8, name="Chemistry, B.S.")
        major_7 = Major.objects.create(department_id_id=3, name="Computer & Information Science, B.S.")
        major_8 = Major.objects.create(department_id_id=10, name="Criminology, B.S.")
        major_10 = Major.objects.create(department_id_id=5, name="General Studies, B.S.")
        major_11 = Major.objects.create(department_id_id=5, name="Health and Society, B.S.")
        major_12 = Major.objects.create(department_id_id=3, name="Management Information Systems, B.S.")
        major_13 = Major.objects.create(department_id_id=6, name="Marketing, B.S.")
        major_14 = Major.objects.create(department_id_id=1, name="Mathematics, B.S.")
        major_15 = Major.objects.create(department_id_id=12, name="Psychology, B.S.")
        major_15 = Major.objects.create(department_id_id=13, name="Sociology, B.S.")
        major_15 = Major.objects.create(department_id_id=4, name="American Studies, B.A.")
        major_15 = Major.objects.create(department_id_id=7, name="Biological Sciences, B.A.")
        major_15 = Major.objects.create(department_id_id=8, name="Chemistry, B.A.")
        major_15 = Major.objects.create(department_id_id=11, name="English, B.A.")
        major_15 = Major.objects.create(department_id_id=4, name="History, B.A.")
        major_15 = Major.objects.create(department_id_id=5, name="Liberal Studies, B.A.")
        major_15 = Major.objects.create(department_id_id=15, name="Media and Communications, B.A.")
        major_15 = Major.objects.create(department_id_id=10, name="Politics, Economics & Law, B.A.")


        # major_requirement_1 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_2 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_3 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_4 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_5 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_6 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_7 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_8 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_9 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_10 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_11 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_12 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_13 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_14 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_15 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_16 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_17 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_18 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_19 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_20 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_21 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_22 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_23 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_24 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_25 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_26 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_27 = MajorRequirement.objects.create(major_id=, course_id=)
        # major_requirement_28 = MajorRequirement.objects.create(major_id=, course_id=)

        minor_1 = Minor.objects.create(department_id_id=6, name="Accounting Minor")
        minor_2 = Minor.objects.create(department_id_id=5, name="African American Studies Minor")
        minor_3 = Minor.objects.create(department_id_id=1, name="Applied Mathematics Minor")
        minor_4 = Minor.objects.create(department_id_id=3, name="Computer and Information Sciences Minor")
        minor_5 = Minor.objects.create(department_id_id=5, name="Congregational Leadership Minor")
        minor_6 = Minor.objects.create(department_id_id=6, name="Digital Design Marketing Minor")
        minor_7 = Minor.objects.create(department_id_id=6, name="Entertainment and Sports Management Minor")
        minor_8 = Minor.objects.create(department_id_id=7, name="Environmental Studies Minor")
        minor_10 = Minor.objects.create(department_id_id=6, name="General Business Minor")
        minor_11 = Minor.objects.create(department_id_id=4, name="Global Studies Minor")
        minor_13 = Minor.objects.create(department_id_id=6, name="Marketing Minor")
        minor_14 = Minor.objects.create(department_id_id=1, name="Mathematics Minor")
        minor_7 = Minor.objects.create(department_id_id=15, name="Media and Communications Minor")
        minor_8 = Minor.objects.create(department_id_id=3, name="Media Design Minor")
        minor_9 = Minor.objects.create(department_id_id=12, name="Neuropsychology Minor")
        minor_10 = Minor.objects.create(department_id_id=10, name="Pre-Law Studies Minor")
        minor_11 = Minor.objects.create(department_id_id=12, name="Psychology Minor")
        minor_12 = Minor.objects.create(department_id_id=5, name="Public Policy Minor")
        minor_13 = Minor.objects.create(department_id_id=13, name="Social Work Minor")