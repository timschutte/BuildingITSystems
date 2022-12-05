from django.db import models

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
    members = models.ManyToManyField(User, through='Membership')
    description = models.TextField()
    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()

def findAppointments(start, end, user):
    return Appointment.objects.get('SELECT * FROM Appointment WHERE (start_time BETWEEN start AND end) OR (end_time BETWEEN start AND end) AND user = user;')

def findAvailability(start, end, name):
    users = Appointment.objects.get('SELECT members FROM Team WHERE name = name;')
    
