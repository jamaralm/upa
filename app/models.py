from django.db import models
from django.db.models import Sum, ExpressionWrapper, F, DurationField
from datetime import datetime

'''
CLASSE SOCIO UPA
'''
class Member(models.Model):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MEMBER = 'MEMBER', 'Membro'

    name = models.CharField(max_length=100, null=False)
    birthday = models.DateField(null=False)
    phone_number = models.CharField(max_length=11, null=False)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)

    def __str__(self):
        return f"{self.name} - {self.calculate_age()} Anos"

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

        return age

'''
CLASSE OFERTINHA DO AMOR
'''
class Contribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="contribuicoes")
    goal = models.ForeignKey("Goal", on_delete=models.PROTECT, related_name="meta", null=True)

    value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    payment_date = models.DateField()
    
    month_reference = models.CharField(max_length=20, help_text="Ex: Abril/2026")

    def __str__(self):
        return f"{self.member} - R${self.value}"
    
'''
CLASSE META DE ARRECADACAO
'''   
class Goal(models.Model):
    name = models.CharField(max_length=100, default="Meta de Arrecadacao")

    value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    start_date = models.DateField(null=True)
    end_date = models.DateField()

    @property
    def value_collected(self):
        value_collected = Contribution.objects.filter(goal=self).aggregate(Sum("value"))['value__sum'] or 0
        value_collected = round(value_collected, 2)
        return value_collected

    @property
    def is_goal_achieved(self, value, value_collected):
        if value_collected >= value:
            return True
        return False

    def __str__(self):
        return f"{self.name} - Meta: R${self.value}"
    
'''
CLASSE EVENTOS 
'''
class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    place = models.CharField(max_length=250)

    confirmed_members = models.ManyToManyField(Member, blank=True, related_name="confirmed_on_event")

    def __str__(self):
        return f"{self.name}"

'''
CLASSE AVISOS 
'''   
class Alert(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"