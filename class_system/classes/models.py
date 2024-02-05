from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta, date
from users.models import CustomUser

class Classes(models.Model):
    AGE_GROUP_CHOICES = (
        ('4-7', '4-7'),
        ('8-11', '8-11'),
    )

    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    
    TIMESLOT_CHOICES = (
        ('11:00-11:50', '11:00-11:50'),
        ('12:00-12:50', '12:00-12:50'),
        ('13:00-13:50', '13:00-13:50'),
        ('14:00-14:50', '14:00-14:50'),
        ('15:00-15:50', '15:00-15:50'),
        ('16:00-16:50', '16:00-16:50'),
        ('17:00-17:50', '17:00-17:50'),
        ('18:00-18:50', '18:00-18:50'),
    )

    title = models.CharField(max_length=100)

    age_group = models.CharField(
        max_length = 10, 
        choices = AGE_GROUP_CHOICES
    )

    day_of_week = models.CharField(
        max_length = 10, 
        choices = DAY_CHOICES
    )

    time_slot = models.CharField(
        max_length = 20,
        choices = TIMESLOT_CHOICES
    )

    start_date = models.DateField(
        default = timezone.now()
    )

    is_active = models.BooleanField(
        default = False
    )

    def __str__(self):
        return f"{self.title} Age {self.age_group} - {self.start_date}"


#enrollments object ready to be implemented
class Enrollments(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('Enrollment Record')

    def __str__(self):
        formatted_date = self.class_enrolled.start_date.strftime("%d %B")
        return f"{self.class_enrolled.title} (Age {self.class_enrolled.age_group}) {formatted_date}"


#manually create the first class, the below method will be triggered to create the same class to the same day of week and time in that month 
@receiver(post_save, sender=Classes)
def auto_create_obj(sender, instance, **kwargs):

    #define the last day of each month
    loop_month_date = instance.start_date
    month_end_date = loop_month_date.replace(day=1) + timedelta(days=32)
    month_end_date = month_end_date.replace(day=1) - timedelta(days=1)

    #assign the start date of the first created object to an individual variable
    start_date = instance.start_date

    #set class_date to 1 day ahead of the first manually created instance so it doesnt duplicate
    loop_month_date = instance.start_date + timedelta(days=1)

    while loop_month_date <= month_end_date:

        if loop_month_date.strftime('%A') == instance.day_of_week:
            #add a week every time the condition and the if statement are fulfilled
            start_date += timedelta(days=7)
            #get the last object created
            last_obj_created = Classes.objects.last()
            #make sure the updated start_date is larger than the last object created start_date before creating next object
            if start_date > last_obj_created.start_date:
                #print(start_date)
                i = Classes(
                    title=instance.title,
                    age_group=instance.age_group,
                    day_of_week=instance.start_date.strftime('%A'),
                    time_slot=instance.time_slot,
                    start_date=start_date,
                    is_active=instance.is_active
                )
                i.save()
        loop_month_date += timedelta(days=1)