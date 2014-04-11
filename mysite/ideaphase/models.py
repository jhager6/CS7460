from django.db import models

# Create your models here.
class UserInfo(models.Model):
     user_id = models.AutoField(primary_key=True)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     user_name = models.CharField(max_length=100)
     password = models.CharField(max_length=100)

class ContestInfo(models.Model):
     contest_id = models.AutoField(primary_key=True)
     contest_name = models.CharField(max_length=100)
     contest_description = models.CharField(max_length=100)
     contest_startdate = models.DateTimeField('Contest start date')
     contest_enddate = models.DateTimeField('Contest end date') 
     contestIdeate_numberAdvance = models.IntegerField(default=0)
     contestDesign_submissionNumberAdvance = models.IntegerField(default=0)

class ContestAssignments(models.Model):
     assignment_id = models.AutoField(primary_key=True)
     contest_id  = models.ForeignKey(ContestInfo)

class ContestStillOpen(models.Model):
     contest_id = models.ForeignKey(ContestInfo)
     contest_enddate = models.DateTimeField('Contest end date')
     ideatephase_enddate = models.DateTimeField('IdeatePhase end date')
     contestIdeate_numberAdvance = models.IntegerField(default=0)

class IdeateIdea(models.Model):
     ideateidea_id = models.AutoField(primary_key=True)
     ideateidea_title = models.CharField(max_length=100)
     user_id = models.ForeignKey(UserInfo)
     contest_id = models.ForeignKey(ContestInfo)
     ideateimage_store_location = models.FileField(upload_to='documents/%Y/%m/%d') 
     ideateidea_date = models.DateTimeField('Ideate Idea Date')  
