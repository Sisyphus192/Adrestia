# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    crse = models.TextField(db_column='Crse', blank=True, null=True)  # Field name made lowercase.
    courseoverall = models.FloatField(db_column='CourseOverall', blank=True, null=True)  # Field name made lowercase.
    hoursperwkinclclass = models.TextField(db_column='HoursPerWkInclClass', blank=True, null=True)  # Field name made lowercase.
    challenge = models.FloatField(db_column='Challenge', blank=True, null=True)  # Field name made lowercase.
    howmuchlearned = models.FloatField(db_column='HowMuchLearned', blank=True, null=True)  # Field name made lowercase.
    crstitle = models.TextField(db_column='CrsTitle', blank=True, null=True)  # Field name made lowercase.
    index = models.AutoField(db_column='index', primary_key=True)

    class Meta:
        managed = False
        db_table = 'courses'

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenge = models.PositiveSmallIntegerField()
    hrsPerWeek = models.PositiveSmallIntegerField()

@receiver(post_save, sender=User)
def create_SiteUser(sender, instance, created, **kwargs):
    if created:
        SiteUser.object.create(user=instance)

@reciever(post_save, sender=User)
def save_SiteUser(sender, instance, **kwargs):
    instance.profile.save()

