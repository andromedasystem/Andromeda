from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


# Create your models here.
class User(models.Model):
    # TODO: Hashing strategy for password
    # TODO: encryption algorithm or nah ? password =
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=70)
    user_type = models.CharField(max_length=1)

    def __str__(self):
        return self.email + "--{ ID: " + self.id + " Name: " + self.first_name \
               + self.last_name + " User_Type: " + self.user_type

    class Meta:
        unique_together = ""


class Admin(models.Model):
    admin_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Student(models.Model):
    student_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date_of_birth = models.DateField()
    student_type = models.CharField(max_length=1)


class FullTimeStudent(models.Model):
    student_id = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    credits = models.IntegerField()


class PartTimeStudent(models.Model):
    student_id = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    credits = models.IntegerField()


class Faculty(models.Model):
    # TODO: add Department FK Constraint when Department Model is created
    faculty_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # TODO: add FK Deparment ID
    faculty_type = models.CharField(max_length=1)


class FullTimeFaculty(models.Model):
    faculty_id = models.OneToOneField(
        Faculty,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class PartTimeFaculty(models.Model):
    faculty_id = models.OneToOneField(
        Faculty,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Researcher(models.Model):
    researcher_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Advising(models.Model):
    advising_id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('faculty_id', 'student_id')


class Hold(models.Model):
    hold_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class StudentHold(models.Model):
    student_hold_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    hold_id = models.ForeignKey(Hold, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student_id', 'hold_id')


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    # TODO: add FK Deparment ID
    name = models.CharField(max_length=254)


class StudentMajor(models.Model):
    student_major_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student_id', 'major_id')


class Minor(models.Model):
    minor_id = models.AutoField(primary_key=True)
    # TODO: add FK Deparment ID
    name = models.CharField(max_length=254)


class StudentMinor(models.Model):
    student_minor_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    minor_id = models.ForeignKey(Minor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student_id', 'minor_id')

# TODO: Student History, Department, Meetings, Enrollment, Section, Course,
# TODO: Major/Minor Requirement, Prerequisite
# TODO: add __str__ methods


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    season = models.CharField(max_length=50)
    year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    type = models.CharField(max_length=35)
    capacity = models.IntegerField()
    room_number = models.CharField(max_length=5)


class MeetingDays(models.Model):
    days_id = models.AutoField(primary_key=True)
    day_1 = models.CharField(max_length=10)
    day_2 = models.CharField(max_length=10)


class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    start_time = models.TimeField(input_formats="%H:%i")
    end_time = models.TimeField(input_formats="%H:%i")


class TimeSlot(models.Model):
    time_slot_id = models.AutoField(primary_key=True)
    days_id = models.ForeignKey(MeetingDays, on_delete=models.CASCADE)
    period_id = models.ForeignKey(Period, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('days_id', 'period_id')
