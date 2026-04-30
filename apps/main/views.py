from django.shortcuts import render
import web.settings as sett
from apps.company.models import Meta_tag_model

# Create your views here.

def media_admin(request):

    context = {
        'media_url':sett.MEDIA_URL
    }

    return context



def main(request):


    meta = Meta_tag_model.objects.filter(is_active = True).first()
    return render(request,'main_app/main.html',{'meta':meta})




def handler400(request, exception):
    return render(request, 'errors/400.html', status=400)

def handler403(request, exception):
    return render(request, 'errors/403.html', status=403)

def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)
