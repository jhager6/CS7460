#builds templates
from django.shortcuts import render
from django.shortcuts import render_to_response

#directs to new pages
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpRequest  

#imports global variables
from django.conf import settings

#loads the data needed for our different views
from ideaphase.models import IdeateIdea
from ideaphase.models import IdeateIdeaComments
from ideaphase.models import UserInfo
from ideaphase.models import ContestInfo
from ideaphase.models import ContestParticipantAssignment
from ideaphase.models import IdeateIdeaComments, IdeateIdeaVote

#loads the forms necessary for uploading information
from ideaphase.forms import IdeateIdeaSubmissionForm, VoteForm
from ideaphase.forms import SystemLogIn

#gets the user's ip address
def get_ip_address(request):
    ip_address = request.META.get['REMOTE_ADDR']
    return ip_address


#checks to see if the user ip address matches that of one in the database
def get_client_ip_check(ip_address):
    try:
        active_user_login = UserInfo.objects.get(ip_address = ip_address)
        return True
    except:
        return False

def list(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)
        
        #handles the file Idea Submission uplaods
        if request.method=='POST':
            submission_form = IdeateIdeaSubmissionForm(request.POST, request.FILES)

            #saves the submission
            if submission_form.is_valid():
                new_submission_store_items = IdeateIdea(ideateimage_store_location = request.FILES['ideateimage_store_location'])
                new_submission_store_items.save()

    ##        submission_save = new_submission_store_items.save(commit=False)
    ##        submssion_save.save()
            
                return HttpResponseRedirect('/ideaphase/list/')
        else:
            submission_form = IdeateIdeaSubmissionForm() #shows empty form

        #Load documents for the list page
        submissions = IdeateIdea.objects.all()
        
        #posts index for html page
        return render_to_response("ideaphase/list.html",
                                  {'submissions':submissions, 'form':submission_form},
                                  context_instance=RequestContext(request)
                                  )

    else:
        return HttpResponseRedirect('ideaphase/home/')


def home(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):
        return HttpResponseRedirect('/ideaphase/profile/')
    else:

        #handles post data from login submission form
        if request.method=='POST':
            
            #create login attempt reques object
            loginattempt = SystemLogIn(request.POST)

            #try's the login attempt
            try:
                #looks up the username that the site user is attempt to log in with
                actual_user = UserInfo.objects.get(user_name=request.POST['username'])
                login_message = ""
            
                #uses the authorization function of the UserInfo Model to authenticiate the user.
                if actual_user.AuthUser(request.POST['username'],request.POST['password']) == True:

                    #save's the ip address for active user tracking
                    actual_user.ip_address = ip_address
                    actual_user.save()
                        
                    #redirects you to the profile page once you have successfully logged in.
                    return HttpResponseRedirect('ideaphase/profile/') 
                else:
                    active_user = UserInfo()
                    login_message = "Incorrect Username or Password"
                    
            #if an error exists in the auth process, you are asked for your stuff again.
            except:
                active_user = UserInfo()
                loginattempt = SystemLogIn()
                login_message = "Incorrect Username or Password"
                
        #if this is a direct hit on the page, asks for your stuff
        else:
            active_user = UserInfo()
            loginattempt = SystemLogIn()
            login_message = ""

        #renders the html document and sends the variables to the templates.                
        return render_to_response("ideaphase/index.html",
                              {"activeuser":active_user, 'form': loginattempt, 'message': login_message},
                              context_instance=RequestContext(request))

def profile(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)
        
        #contest that user is currenntly assigned to 
        current_contest = ContestParticipantAssignment.objects.filter(user_id = active_user.user_id)

        #gets all the active contest in the system
        #now = datetime.datetime.now()
        #current_contest = ContestInfo.objects.filter(contest_enddate >= now).filter(contest_startdate <= now)

    else:
        return HttpResponseRedirect('ideaphase/home/')
        
    return render_to_response("ideaphase/profile.html",
                              {'ActiveUser':active_user, 'CurrentContest':current_contest },
                              context_instance=RequestContext(request))

def logout(request):
    ip_address = request.get_host()
    active_user = UserInfo.objects.get(ip_address=ip_address)

    #sets the ip_address to zero so the user is logged out
    active_user.ip_address = 0
    active_user.save()
    
    return render_to_response("ideaphase/logout.html",
                              locals(),
                              context_instance=RequestContext(request))

def browse_contest_ideas(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)


    #your view code goes here


    else:
        return HttpResponseRedirect('ideaphase/home/')
      
    return render_to_response("ideaphase/browse_contest_ideas.html",
                              {'ActiveUser':active_user},
                              context_instance=RequestContext(request))



def contest_main(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)

        #pulls the contest information for the user contests
        try:
            #creates a dictionary of ContestInfo objects
            #to list the contests the user is in/ not in
            my_contests = ContestParticipantAssignment.objects.filter(user_id = active_user.user_id)

            #creates a list of ContestInfo Objects to differentiate between current user contests and other contests
            #not signed up for.
            if not my_contests:
                other_contests = ContestInfo.objects.all()
            else:
                all_contests = ContestInfo.objects.all()
                other_contests=[]
                for my_contest in my_contests:
                    for contest in all_contests:
                        if contest.contest_id == my_contest.contest_id.contest_id:
                            other_contests = other_contests
                        else:
                            other_contests.append(contest)

        except:
            my_contests = ""
            other_contests = ContestInfo.objects.all()


    else:
        return HttpResponseRedirect('ideaphase/home/')
      
    return render_to_response("ideaphase/contests_main.html",
                              {'ActiveUser':active_user,
                               'my_contests':my_contests,
                               'other_contests':other_contests},
                              context_instance=RequestContext(request))



def profile_my_submissions(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)


    #your view code goes here


    else:
        return HttpResponseRedirect('ideaphase/home/')
      
    return render_to_response("ideaphase/profile_my_submissions.html",
                              {'ActiveUser':active_user},
                              context_instance=RequestContext(request))


def submit_idea(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
        ip_address = request.get_host()
        if get_client_ip_check(ip_address):

            #grabs the active user information and loads it into the view
            active_user = UserInfo.objects.get(ip_address=ip_address)

            #your view code goes here
            #Jon: Okay!

            #ID of the contest you want to submit ideas to
            


            if request.method=='POST':
                    submission_form = IdeateIdeaSubmissionForm(request.POST, request.FILES)
                    contest_id = request.POST['contest_id']
                    first_nav = request.POST['first_nav']

                    contest_click = ContestInfo.objects.get(contest_id = contest_id)

                    #if the user assignment does not exist, a new assignment is created
                    #if the user assignment exists, then it sets the user_contest_assignment_info variable
                    try:
                        user_contest_assignment_info = ContestParticipantAssignment.objects.get(user_id = active_user.user_id, contest_id=contest_click)
                    except:
                        #assigns the user to the current contest if the clicked the 'sign up and submit' button
                        sign_up_user = ContestParticipantAssignment()
                        sign_up_user.contest_id = contest_click
                        sign_up_user.user_id = active_user
                        sign_up_user.save()

                        #assigns the user to user_contest_assignment_info variable
                        user_contest_assignment_info = sign_up_user


                    #if submission_form.is_valid():
                    if submission_form.is_valid():
                        new_submission_store_items = IdeateIdea(ideateimage_store_location = request.FILES['ideateimage_store_location'],
                                                                ideateidea_title = request.POST['ideateidea_title'],
                                                                user_id = user_contest_assignment_info.user_id,
                                                                contest_id = user_contest_assignment_info.contest_id,
                                                                ideateidea_description = 'description save error')
                        #new_submission_store_items.ideateimage_store_location = request.FILES['ideateimage_store_location']
                        #new_submission_store_items.ideateidea_title = request.POST['ideateidea_title']
                        #new_submission_store_items.user_id = active_user.user_id
                        #new_submission_store_items.contest_id = contest_id
                        #new_submission_store_items.ideateidea_description = 'description save error' ###request.POST['ideateidea_description']                                                                                                                                                              ideateidea_title = request.POST['ideateidea_title'],                                                                                                                                                                ideateidea_description = request.POST['ideatedesc_store'],)			

                        new_submission_store_items.save()


                        return HttpResponseRedirect('/ideaphase/contest_landing_page/')
                                
                    else:
                        first_nav = 0
                        submission_form = IdeateIdeaSubmissionForm()#shows empty form
                    

            else:
                #This block will only be executed if the user navigated directly to this page.
                submission_form = IdeateIdeaSubmissionForm() #shows empty form
                contest_id = 1	    
                val = "no HTTP POST"
                first_nav = 1
                return HttpResponseRedirect('/ideaphase/contest_landing_page/')
    
	else:
            #User is not logged in
	    return HttpResponseRedirect('ideaphase/home/')
      
	return render_to_response("ideaphase/submit_idea.html",
                              {'ActiveUser':active_user,
                               'form': submission_form,
                               'contest_id': contest_id},
                              context_instance=RequestContext(request))



def contest_landing_page(request):
    #Handles User Login Attempt
    #Used on all views to verify login information.
    #Due to time constraints, this is acting as our persistence layer
    ip_address = request.get_host()
    if get_client_ip_check(ip_address):

        #grabs the active user information and loads it into the view
        active_user = UserInfo.objects.get(ip_address=ip_address)

        #if a button is clicked on contest main, it posts the variable
        if request.method=='POST':
            contest_click = request.POST['contest_id']
            contest_id = ContestInfo.objects.get(contest_id = contest_click)
            ideate_ideas_to_display = IdeateIdea.objects.filter(contest_id = contest_id)


            TheFinalTruth = request.POST['vote_submit']
            post_value = request.POST['vote_submit']
##            if post_value==2:
##                try:
                #initializes post data
            try:
                idea_vote = request.POST['vote']
                ideate_id = request.POST['ideate_id']
        
                #creates and updates a IdeateIdeaVote object
                idea_vote_entry = IdeateIdeaVote(idea_vote = request.POST['vote'],
                                             user_id = active_user,
                                             contest_id = contest_id,
                                             ideate_id = request.POST['ideate_id'])
                
            
                #saves the vote
                if idea_vote_entry.is_valid():
                    idea_vote_entry.save()
                    TheFinalTruth = "WIN!"
                else:
                    TheFinalTruth = "EPIC FAIL!!!"

            except:
                import sys
                TheFinalTruth = 'fail of the post try'
            

                
            


            
            return render_to_response('ideaphase/contest_landing_page.html',
                                      {'contest_id': contest_click,
                                       'ideas': ideate_ideas_to_display,
                                       'contest': contest_id,
                                       'TheFinalTruth': TheFinalTruth},
                                      context_instance=RequestContext(request))



        else:
            #the user navigated directly to this page.
            return HttpResponseRedirect('ideaphase/contests_main/')
    else:
        return HttpResponseRedirect('ideaphase/home/')
      
    return render_to_response("ideaphase/contest_landing_page.html",
                              {'ActiveUser':active_user},
                              context_instance=RequestContext(request))

## view template below:
##def view_template(request):
##    #Handles User Login Attempt
##    #Used on all views to verify login information.
##    #Due to time constraints, this is acting as our persistence layer
##    ip_address = request.get_host()
##    if get_client_ip_check(ip_address):
##
##        #grabs the active user information and loads it into the view
##        active_user = UserInfo.objects.get(ip_address=ip_address)


##    #your view code goes here

##
##    else:
##        return HttpResponseRedirect('ideaphase/home/')
##      
##    return render_to_response("ideaphase/template.html",
##                              {'ActiveUser':active_user},
##                              context_instance=RequestContext(request))

