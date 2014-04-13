from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#loads the data needed for our different views
from ideaphase.models import IdeateIdea
from ideaphase.models import IdeateIdeaComments

#loads the forms necessary for uploading information
from ideaphase.forms import IdeateIdeaForm
from ideaphase.forms import IdeateIdeaSubmissionForm


def list(request):
    #handles the file Idea Submission uplaods
    submission_form = IdeateIdeaSubmissionForm(request.POST, request.FILES)

    #saves the submission
    if submission_form.is_valid():
        new_ideateimage_store_location = IdeateIdea(ideateimage_store_location = request.FILES['ideateimage_store_location'],
                                                    ideatedesc_store = request.POST['ideateidea_description'])
        new_ideateimage_store_location.save()    
        return HttpResponseRedirect(reverse('ideaphase.views.list'))
    else:
        form = IdeateIdeaForm() #shows empty form

    #Load documents for the list page
    documents = IdeateIdea.objects.all()
    
    #posts index for html page
    return render_to_response("ideaphase/list.html",
                              locals(),
                              context_instance=RequestContext(request,
                                                              {'documents':documents, 'form':submission_form}))

def home(request):
    return render_to_response("ideaphase/index.html",
                              locals(),
                              context_instance=RequestContext(request))

