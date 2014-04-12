from django.shortcuts import render


def overwrite_view_here(self):
    return 1

m django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_ideateimage_store_location = Document(ideateimage_store_location = request.FILES['ideateimage_store_location'])
            new_ideateimage_store_location.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('ideaphase.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'ideaphase/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


