# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Courses(models.Model):
<<<<<<< HEAD
    yearterm = models.BigIntegerField(db_column='Yearterm', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    crse = models.BigIntegerField(db_column='Crse', blank=True, null=True)  # Field name made lowercase.
    sec = models.TextField(db_column='Sec', blank=True, null=True)  # Field name made lowercase.
    onlinefcq = models.TextField(db_column='OnlineFCQ', blank=True, null=True)  # Field name made lowercase.
    bdcontinedcrse = models.FloatField(db_column='BDContinEdCrse', blank=True, null=True)  # Field name made lowercase.
    instructor = models.TextField(db_column='Instructor', blank=True, null=True)  # Field name made lowercase.
    formsrequested = models.BigIntegerField(db_column='FormsRequested', blank=True, null=True)  # Field name made lowercase.
    formsreturned = models.BigIntegerField(db_column='FormsReturned', blank=True, null=True)  # Field name made lowercase.
    courseoverallpctvalid = models.TextField(db_column='CourseOverallPctValid', blank=True, null=True)  # Field name made lowercase.
    courseoverall = models.FloatField(db_column='CourseOverall', blank=True, null=True)  # Field name made lowercase.
    courseoverall_sd = models.FloatField(db_column='CourseOverall_SD', blank=True, null=True)  # Field name made lowercase.
    instructoroverall = models.FloatField(db_column='InstructorOverall', blank=True, null=True)  # Field name made lowercase.
    instructoroverall_sd = models.FloatField(db_column='InstructorOverall_SD', blank=True, null=True)  # Field name made lowercase.
    hoursperwkinclclass = models.TextField(db_column='HoursPerWkInclClass', blank=True, null=True)  # Field name made lowercase.
    priorinterest = models.FloatField(db_column='PriorInterest', blank=True, null=True)  # Field name made lowercase.
    instreffective = models.FloatField(db_column='InstrEffective', blank=True, null=True)  # Field name made lowercase.
    availability = models.FloatField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    challenge = models.FloatField(db_column='Challenge', blank=True, null=True)  # Field name made lowercase.
    howmuchlearned = models.FloatField(db_column='HowMuchLearned', blank=True, null=True)  # Field name made lowercase.
    instrrespect = models.FloatField(db_column='InstrRespect', blank=True, null=True)  # Field name made lowercase.
    crstitle = models.TextField(db_column='CrsTitle', blank=True, null=True)  # Field name made lowercase.
    r_presnt = models.FloatField(db_column='R_Presnt', blank=True, null=True)  # Field name made lowercase.
    r_fair = models.FloatField(db_column='R_Fair', blank=True, null=True)  # Field name made lowercase.
    workload = models.FloatField(db_column='Workload', blank=True, null=True)  # Field name made lowercase.
    r_divstu = models.FloatField(db_column='R_Divstu', blank=True, null=True)  # Field name made lowercase.
    r_access = models.FloatField(db_column='R_Access', blank=True, null=True)  # Field name made lowercase.
    r_learn = models.FloatField(db_column='R_Learn', blank=True, null=True)  # Field name made lowercase.
    campus = models.TextField(db_column='Campus', blank=True, null=True)  # Field name made lowercase.
    college = models.TextField(db_column='College', blank=True, null=True)  # Field name made lowercase.
    asdiv = models.TextField(db_column='ASdiv', blank=True, null=True)  # Field name made lowercase.
    level = models.TextField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    fcqdept = models.TextField(db_column='Fcqdept', blank=True, null=True)  # Field name made lowercase.
    instr_group = models.TextField(db_column='Instr_Group', blank=True, null=True)  # Field name made lowercase.
    i_num = models.BigIntegerField(db_column='I_Num', blank=True, null=True)  # Field name made lowercase.
    crse_id = models.BigIntegerField(db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'courses'
=======
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    crse = models.BigIntegerField(db_column='Crse', blank=True, null=True)  # Field name made lowercase.
    courseoverall = models.FloatField(db_column='CourseOverall', blank=True, null=True)  # Field name made lowercase.
    hoursperwkinclclass = models.TextField(db_column='HoursPerWkInclClass', blank=True, null=True)  # Field name made lowercase.
    challenge = models.FloatField(db_column='Challenge', blank=True, null=True)  # Field name made lowercase.
    howmuchlearned = models.FloatField(db_column='HowMuchLearned', blank=True, null=True)  # Field name made lowercase.
    crstitle = models.TextField(db_column='CrsTitle', blank=True, null=True)  # Field name made lowercase.
    index = models.AutoField(db_column='index', primary_key=True)

    class Meta:
        managed = False
        db_table = 'simplified_courses'
>>>>>>> 2de504f43a4cb4a778e0f93ec74189ef8dc1c01f
