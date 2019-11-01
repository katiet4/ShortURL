from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SandFURL
from .GSURL import generateSURL
import requests
from django.utils import timezone
# Create your views here.

def renderSite(request, authenticated):
        host = request.get_host()
        color = 'green'
        if request.POST:
            url = request.POST['url']

            try:
                req = requests.get(url)
                surl = generateSURL(SandFURL)
                if(authenticated):
                    sandfurl = SandFURL(username = request.user.username, FURL = url, SURL = surl)
                    sandfurl.save()
                else:
                    sandfurl = SandFURL(username = "", FURL = url, SURL = surl)
                    sandfurl.save()
                    return render(request, 'MSURLTemp/MSURL.html',{'urlsAnon':[url, host+'/'+surl, str(0), timezone.now()],'style':""})
            except Exception as e:
                color = 'red'
                print(e)
            else:
                color = 'red'

            #hello
        style = "color:"+color+";" if color == 'red' else ""
        if(authenticated):
            if (SandFURL.objects.filter(username = request.user.username).exists()):
                return render(request, 'MSURLTemp/MSURL.html',
                                { "urls": SandFURL.objects.filter(username = request.user.username),
                                'style':style, "aunt": True,'host':host+'/'})
            else:
                return render(request, 'MSURLTemp/MSURL.html',{'style':style, "aunt": True})
        return render(request, 'MSURLTemp/MSURL.html',{'style':style})

def MSURL(request):
    if request.user.is_authenticated:
        return renderSite(request, True)
    else:
        return renderSite(request, False)
