from django.shortcuts import render
from django.http import HttpResponseRedirect
from MakeShortURL.models import SandFURL

def redirect(request, IDHash):
    if (SandFURL.objects.filter(SURL = IDHash).exists()):
        link = SandFURL.objects.get(SURL = IDHash)
        link.howlongUsed += 1
        linkCopy = link.FURL
        link.save()
        return HttpResponseRedirect(linkCopy)
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/msurl")
        else:
            return HttpResponseRedirect("/login")
# Create your views here.
