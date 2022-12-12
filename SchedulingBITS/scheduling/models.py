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

def createAppointment(name, user: User, start_time: datetime, end_time: datetime, description='', location='', hyperlink=''):
    Appointment.objects.create(name=name, user=user, description=description, start_time=int(datetime.timestamp(start_time)), end_time=int(datetime.timestamp(end_time)), location=location, hyperlink=hyperlink)
# A function to return all times for a certain user within a certain timeframe
# Can be used to render a calendar
def findAppointments(start_time: datetime, end_time: datetime, user: User):
    c = conn.cursor()
    try:
        id = user.id
    except AttributeError:
        id = user
    c.execute(f'SELECT * FROM scheduling_appointment WHERE ((start_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())}) OR (end_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())})) AND user_id = {id};')
    data = c.fetchall()
    c.close()
    return data

# A function to return all TIMES (only the start and end time of existing appointments) for a certain team within a certain timeframe
# Can be used for availability checking
def returnAppointmentsTeam(start_time: datetime, end_time: datetime, team: Team):
    c = conn.cursor()
    c.execute(f'SELECT start_time, end_time, user_id FROM (SELECT A.start_time, A.end_time, A.user_id FROM scheduling_appointment A, scheduling_membership M WHERE M.user_id = A.user_id AND M.team_id = {team}) WHERE (start_time BETWEEN {start_time.timestamp()} AND {end_time.timestamp()}) OR (end_time BETWEEN {start_time.timestamp()} AND {end_time.timestamp()}) ORDER BY start_time ASC;')
    data = c.fetchall()
    c.close()
    return data

######## The sorting is done by indexing the starting time! IF ANYTHING CHANGES TO THE COLUMN ORDER OF THE APPOINTMENTS TABLE, THIS WILL BREAK
# In that case i_start and i_end need to be adjusted accordingly ########
i_start = 0
i_end = 1
def availabilityPercentage(start_time: datetime, end_time: datetime, team: Team):
    sorted_ap = returnAppointmentsTeam(start_time, end_time, team) # sorted appointments
    team_percentage = 1 / Membership.objects.filter(team=team).count() # The percentage of the team one team member represents
    availability = [[time, 1] for time in range(int(start_time.timestamp()) - int(start_time.timestamp()) % 900, int(end_time.timestamp()) - int(end_time.timestamp()) % 900, 900)] # The time interval buckets of 15 minute intervals with initialized percentage of avialability
    # The following two loops are to make sure that the appointments are within the timeframe
    for i in range(len(sorted_ap)):
        if sorted_ap[i][i_start] < start_time.timestamp():
            sorted_ap[i][i_start] = start_time.timestamp()
        else:
            break

    for i in range(len(sorted_ap) -1 , -1, -1):
        if sorted_ap[i][i_end] > end_time.timestamp():
            sorted_ap[i][i_end] = end_time.timestamp()
    latest_timebucket = 0

    for i in range(len(sorted_ap)):
        for i1 in range(latest_timebucket, len(availability)):
            ###### Just realized that if someone has two overlapping appointments, this will lower the availability twice. 
            if sorted_ap[i][i_start] < availability[i1][0]+900:
                if sorted_ap[i][i_end] > availability[i1][0]:
                    availability[i1][1] -= team_percentage
            elif sorted_ap[i][i_start] >= availability[i1][0] + 900: # For shortening outer loop for runtime performance
                latest_timebucket = i1 + 1
                continue
            elif sorted_ap[i][i_end] <= availability[i1][0]: # For cutting loops of short if possible for runtime performance
                break
    return availability


