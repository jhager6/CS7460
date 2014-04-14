from django.contrib import admin
from ideaphase.models import UserInfo,ContestInfo,ContestParticipantAssignment,ContestStillOpen,IdeateIdea,IdeateIdeaComments,IdeateIdeaVote


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(ContestInfo)
admin.site.register(ContestParticipantAssignment)
admin.site.register(ContestStillOpen)
admin.site.register(IdeateIdea)
admin.site.register(IdeateIdeaComments)
admin.site.register(IdeateIdeaVote)

    
