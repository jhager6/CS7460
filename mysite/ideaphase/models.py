from django.db import models
 
#creates a UserInfo Table
#the table inherits attributes from the user AUTH user class.
class UserInfo(models.Model):     
     user_id = models.AutoField(primary_key=True) 
     first_name = models.CharField(max_length=100) 
     last_name = models.CharField(max_length=100) 
     user_name = models.CharField(max_length=100, unique=True)
     email = models.EmailField(blank=True)
     password = models.CharField(max_length=100)
     ip_address = models.TextField()

     def AuthUser(self,user_attempt,pass_attempt):
          self_user_concat = self.user_name + self.password
          attempt_user_concat = user_attempt + pass_attempt
          if self_user_concat == attempt_user_concat:
               return True
          else:
               return False
     
class ContestInfo(models.Model): 
     contest_id = models.AutoField(primary_key=True) 
     contest_name = models.CharField(max_length=100) 
     contest_description = models.CharField(max_length=100) 
     contest_startdate = models.DateTimeField() 
     contest_enddate = models.DateTimeField() 
     contestIdeate_numberAdvance = models.IntegerField(default=0) 
     contestDesign_submissionNumberAdvance = models.IntegerField(default=0)
     
class ContestParticipantAssignment(models.Model): 
     assignment_id = models.AutoField(primary_key=True) 
     contest_id  = models.ForeignKey(ContestInfo) 
     user_id = models.ForeignKey(UserInfo)
     
class ContestStillOpen(models.Model): 
     contest_id = models.ForeignKey(ContestInfo) 
     contest_enddate = models.DateTimeField() 
     ideatephase_enddate = models.DateTimeField() 
     contestIdeate_numberAdvance = models.IntegerField(default=0)
     
class IdeateIdea(models.Model): 
     ideate_id = models.AutoField(primary_key=True) 
     ideateidea_title = models.CharField(max_length=100) 
     user_id = models.ForeignKey(UserInfo) 
     contest_id = models.ForeignKey(ContestInfo) 
     ideateimage_store_location = models.FileField(upload_to='documents/%Y/%m/%d') 
     ideateidea_date = models.DateTimeField(auto_now_add=True, blank=True)
     ideateidea_description = models.CharField(max_length=500)
     
class IdeateIdeaComments(models.Model): 
     comment_id = models.AutoField(primary_key=True) 
     ideate_id = models.ForeignKey(IdeateIdea) 
     comment_information = models.CharField(max_length=250) 
     user_id = models.ForeignKey(UserInfo) 
     ideateidea_commentdate = models.DateTimeField(auto_now_add=True)
 
class IdeateIdeaVote(models.Model): 
     ideatevote_id = models.AutoField(primary_key=True) 
     user_id = models.ForeignKey(UserInfo) 
     ideate_id = models.ForeignKey(IdeateIdea) 
     ideateidea_date = models.DateTimeField(auto_now_add=True, blank=True) 
     IDEATE_IDEA__VOTE = ( 
           ('Y', 'Yes'), 
           ('N', 'No'), 
          ) 
     ideate_vote = models.CharField(max_length=1, choices=IDEATE_IDEA__VOTE)

