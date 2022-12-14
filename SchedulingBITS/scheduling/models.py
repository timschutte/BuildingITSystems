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

i_ap ={'id':0, 'name':1, 'description':2, 'end_time':3, 'location':4, 'hyperlink':5, 'user_id':6, 'start_time':7}
def editAppointment(appointment, name=None, start_time=None, end_time=None, description=None, location=None, hyperlink=None):
    if name is None:
        name = appointment[i_ap['name']]
    if start_time is None:
        start_time = int(datetime.timestamp(appointment[i_ap['start_time']]))
    if end_time is None:
        end_time = int(datetime.timestamp(appointment[i_ap['end_time']]))
    if hyperlink is None:
        hyperlink = appointment[i_ap['hyperlink']]
    if description is None:
        description = appointment[i_ap['description']]
    if location is None:
        location = appointment[i_ap['location']]
    c = conn.cursor()
    c.execute('UPDATE scheduling_appointment SET name = ?, start_time = ?, end_time = ?, description = ?, location = ?, hyperlink = ? WHERE id = ?;', (name, start_time, end_time, description, location, hyperlink, appointment.id))
    c.close()

def returnAppointmentsUser(start_time: datetime, end_time: datetime, user: User, full_ap=False):
    c = conn.cursor()
    try:
        id = user.id
    except AttributeError:
        id = user
    if full_ap:
        c.execute(f'SELECT * FROM scheduling_appointment WHERE ((start_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())}) OR (end_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())})) AND user_id = {int(id)};')
    else:
        c.execute(f'SELECT start_time, end_time, user_id FROM scheduling_appointment WHERE ((start_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())}) OR (end_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())})) AND user_id = {int(id)};')
    data = c.fetchall()
    c.close()
    return data

# A function to return all TIMES (only the start and end time of existing appointments) for a certain team within a certain timeframe
# Can be used for availability checking
def returnAppointmentsTeam(start_time: datetime, end_time: datetime, team: Team):
    c = conn.cursor()
    #query = f"SELECT start_time, end_time, user_id FROM (SELECT A.start_time , A.end_time, A.user_id  FROM scheduling_appointment A, scheduling_membership M WHERE M.user_id = A.user_id AND M.team_id = {team}) WHERE start_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())} OR end_time BETWEEN {int(start_time.timestamp())} AND {int(end_time.timestamp())} ORDER BY start_time ASC;"
    query = f"SELECT user_id from scheduling_membership WHERE team_id = {team};"
    c.execute(query)
    users = c.fetchall()
    c.close()
    appointments = []
    for user in users:
        appointments_user = returnAppointmentsUser(start_time, end_time, user[0])
        if appointments_user != []:
            appointments.append(appointments_user)
    return appointments


def deleteOverlap(appointments):
    for i in range(len(appointments)-1, 0, -1):
        if appointments[i][i_start] <= appointments[i-1][i_end]:
            appointments[i-1] = (appointments[i-1][i_start], max(appointments[i][i_end], appointments[i-1][i_end]), appointments[i-1][-1])
            del appointments[i]
    return appointments
            
i_start = 0
i_end = 1
def substractAvailabilityUser(availability, appointments, team_percentage):
    latest_timebucket = 0
    for i in range(len(appointments)):
        for i1 in range(latest_timebucket, len(availability)):
            if appointments[i][i_start] < availability[i1][0]+900:
                if appointments[i][i_end] > availability[i1][0]:
                    availability[i1][1] -= team_percentage
            elif appointments[i][i_start] >= availability[i1][0] + 900: # For shortening outer loop for runtime performance
                latest_timebucket = i1 + 1
                continue
            elif appointments[i][i_end] <= availability[i1][0]: # For cutting loops of short if possible for runtime performance
                break
    return availability


def availabilityPercentageTeam(start_time: datetime, end_time: datetime, team: Team): 
    team_percentage = 1 / Membership.objects.filter(team=team).count() # The percentage of the team one team member represents
    availability = [[time, 1] for time in range(int(start_time.timestamp()) - int(start_time.timestamp()) % 900, int(end_time.timestamp()) - int(end_time.timestamp()) % 900, 900)] # The time interval buckets of 15 minute intervals with initialized percentage of avialability
    appointments_team = returnAppointmentsTeam(start_time, end_time, team)
    for appointments_user in appointments_team:
        appointments_user = deleteOverlap(appointments_user)
        availability = substractAvailabilityUser(availability, appointments_user, team_percentage)
    return availability
