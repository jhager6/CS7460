from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#loads the data needed for our different views
from ideaphase.models import IdeateIdea
from ideaphase.models import IdeateIdeaComments

#loads the forms necessary for uploading information
from ideaphase.forms import IdeateIdeaSubmissionForm


def list(request):
    #handles the file Idea Submission uplaods
    if request.method=='POST':
        submission_form = IdeateIdeaSubmissionForm(request.POST, request.FILES)

        #saves the submission
        if submission_form.is_valid():
            new_submission_store_items = IdeateIdea(ideateimage_store_location = request.FILES['ideateimage_store_location'])
            new_submission_store_items.save()

##        submission_save = new_submission_store_items.save(commit=False)
##        submssion_save.save()
        
            return HttpResponseRedirect(reverse('ideaphase.views.list'))
    else:
        submission_form = IdeateIdeaSubmissionForm() #shows empty form

    #Load documents for the list page
    submissions = IdeateIdea.objects.all()
    
    #posts index for html page
    return render_to_response("ideaphase/list.html",
                              {'submissions':submissions, 'form':submission_form},
                              context_instance=RequestContext(request)
                              )

def home(request):
    return render_to_response("ideaphase/index.html",
                              locals(),
                              context_instance=RequestContext(request))

def profile(request):
    return render_to_response("ideaphase/profile.html",
                              locals(),
                              context_instance=RequestContext(request))

