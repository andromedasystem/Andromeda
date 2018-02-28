from django.db import models


# Create your models here.
class User(models.Model):
    # TODO: Hashing strategy for password
    # TODO: encryption algorithm or nah ? password =
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
    email = models.ForeignKey(User, to_field="email", db_column="email")
    password = models.ForeignKey(User, to_field="password", db_column="password")
    first_name = models.ForeignKey(User, to_field="first_name", db_column="first_name")
    last_name = models.ForeignKey(User, to_field="last_name", db_column="last_name")


class Student(models.Model):
    email = models.ForeignKey(User, to_field="email", db_column="email")
    password = models.ForeignKey(User, to_field="password", db_column="password")
    first_name = models.ForeignKey(User, to_field="first_name", db_column="first_name")
    last_name = models.ForeignKey(User, to_field="last_name", db_column="last_name")
    date_of_birth = models.DateField()
    student_type = models.CharField(max_length=1)


class Faculty(models.Model):
    # TODO: add Department FK Constraint when Department Model is created
    email = models.ForeignKey(User, to_field="email", db_column="email")
    password = models.ForeignKey(User, to_field="password", db_column="password")
    first_name = models.ForeignKey(User, to_field="first_name", db_column="first_name")
    last_name = models.ForeignKey(User, to_field="last_name", db_column="last_name")
    # TODO: add FK Deparment ID
    faculty_type = models.CharField(max_length=1)


class Researcher(models.Model):
    email = models.ForeignKey(User, to_field="email", db_column="email")
    password = models.ForeignKey(User, to_field="password", db_column="password")
    first_name = models.ForeignKey(User, to_field="first_name", db_column="first_name")
    last_name = models.ForeignKey(User, to_field="last_name", db_column="last_name")