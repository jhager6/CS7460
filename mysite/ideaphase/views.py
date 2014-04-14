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

#loads the forms necessary for uploading information
from ideaphase.forms import IdeateIdeaSubmissionForm
from ideaphase.forms import SystemLogIn

#gets the user's ip address

def get_ip_address(request):
    ip_address = request.META.get['REMOTE_ADDR']
    return ip_address

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
    return render_to_response("ideaphase/profile.html",
                              locals(),
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
##        return render_to_response("ideaphase/template.html",
##                              locals(),
##                              context_instance=RequestContext(request))

