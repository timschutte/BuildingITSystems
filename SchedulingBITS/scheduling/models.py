from django.db import models
from datetime import datetime
import sqlite3


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    location = models.CharField(max_length=100)
    hyperlink = models.URLField()
    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name + " " + self.team.name



conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


def createAppointment(name, user: User, description, start_time: datetime, end_time: datetime, location, hyperlink):
    Appointment.objects.create(name=name, user=user, description=description, start_time=int(datetime.timestamp(start_time)), end_time=int(datetime.timestamp(end_time)), location=location, hyperlink=hyperlink)
# A function to return all times for a certain user within a certain timeframe
# Can be used to render a calendar
def findAppointments(start_time: datetime, end_time: datetime, user: User):
    try:
        id = user.id
    except AttributeError:
        id = user
    c.execute(f'SELECT * FROM scheduling_appointment WHERE ((start_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())}) OR (end_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())})) AND user_id = {id};')
    return c.fetchall()

# A function to return all TIMES (only the start and end time of existing appointments) for a certain team within a certain timeframe
# Can be used for availability checking
def returnAppointmentsTeam(start_time: datetime, end_time: datetime, team: Team):
    c.execute(f'SELCECT start_time, end_time FROM (SELECT A.start_time, A.end_time FROM scheduling_appointment A, scheduling_membership M WHERE M.user_id = A.user_id AND M.team_id = {team}) WHERE (start_time BETWEEN {start_time.timestamp()} AND {end_time.timestamp()}) OR (end_time BETWEEN {start_time.timestamp()} AND {end_time.timestamp()});')
    return c.fetchall() 


