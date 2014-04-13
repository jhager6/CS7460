from django import forms

class IdeateIdeaForm(forms.Form):
    ideateimage_store_location = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class IdeateIdeaSubmissionForm(forms.Form):
    ideateimage_store_location = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

    ideatedesc_store = forms.CharField(
        widget = forms.Textarea,
        label='Describe your submission',
        help_text='max. 500 characters',
        )

class IdeateIdeaCommentSubmissionForm(forms.Form):
    ideateidea_comment_store = forms.CharField(
        label='What do you think of this idea?'
        )

class IdeateIdeaVoteSubmission(forms.Form):
    ideateidea_vote_store = forms.DateTimeField()
    
