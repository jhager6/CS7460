from django import forms

#creates the idea submission form
class IdeateIdeaSubmissionForm(forms.Form):

        ideateidea_title = forms.CharField(
		label = 'Submission title',
		help_text = ''
		)

	ideateimage_store_location = forms.ImageField(
                label='Select a file',
                help_text='max. 42 megabytes'
                )

	ideateidea_description = forms.CharField(
                widget = forms.Textarea,
                label='Describe your submission',
                help_text='max. 500 characters'
                )

#creates the foreign user comment form
class IdeateIdeaCommentSubmissionForm(forms.Form):
        ideateidea_comment_store = forms.CharField(
                label='What do you think of this idea?'
                )

#creates the voting form
class IdeateIdeaVoteSubmission(forms.Form):
        ideateidea_vote_store = forms.DateTimeField()

class SystemLogIn(forms.Form):
        username = forms.CharField(
                label='Username'
                )
        password = forms.CharField(
                label='Password'
                )

    
