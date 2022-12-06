from django.db import models
from datetime import datetime


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
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    hyperlink = models.URLField()
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name + " " + self.team.name

# A function to return all times for a certain user within a certain timeframe
# Can be used to render a calendar
def findAppointments(start, end, user):
    return Appointment.objects.get(f'SELECT * FROM Appointment WHERE (start_time BETWEEN {start} AND {end}) OR (end_time BETWEEN {start} AND {end}) AND user = {user};')

# A function to return all TIMES (only the start and end time of existing appointments) for a certain team within a certain timeframe
# Can be used for availability checking
def returnAppointmentsTeam(start, end, team):
    return Appointment.objects.get(f'SELCECT start_time, end_time FROM (SELECT A.start_time, A.end_time FROM Appointment A, Membership M WHERE M.user = A.user AND M.team = {team}) WHERE (start_time BETWEEN {start} AND {end}) OR (end_time BETWEEN {start} AND {end});')
    
