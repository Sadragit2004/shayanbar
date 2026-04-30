from django.shortcuts import render
from .models import Comment,text_description2,text_description,ProjectModel,Company,Slider_main,MediaUrl,WhyUs,ResumCompany,Meta_tag_model
# Create your views here.


def get_active_companies():
    """
    Retrieves all active companies from the database.

    Returns:
        QuerySet: Active companies.
    """
    return Company.objects.filter(is_active=True)



def show_name(request):

    company = get_active_companies()
    return render(request,'partials/plus/name.html',{'company':company})



def show_phone_number(request):

    company = get_active_companies()
    return render(request,'partials/plus/phone_number.html',{'company':company})


def show_mobile_number(request):

    company = get_active_companies()
    return render(request,'partials/plus/mobile_number.html',{'company':company})





def show_address(request):

    company = get_active_companies()
    return render(request,'partials/plus/address.html',{'company':company})



def show_video(request):

    company = get_active_companies()
    return render(request,'partials/plus/video.html',{'company':company})



def time_work(request):

    company = get_active_companies()
    return render(request,'partials/plus/time_work.html',{'company':company})



def show_logo(request):

    company = get_active_companies()
    return render(request,'partials/plus/logo.html',{'company':company})




def sliders(request):

    Slider_mains = Slider_main.objects.filter(is_active = True).order_by('-create_at')
    return render(request,'partials/plus/sliders.html',{'sliders':Slider_mains})




def SociaMediaview(request):

    SociaMedias = MediaUrl.objects.filter(is_active = True).order_by('-create_at')
    return render(request,'partials/plus/sociaMedia.html',{'social_media':SociaMedias})





def WhyUsBox(request):

    why_us = WhyUs.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'why_us/why_us.html',{'whys':why_us})




def show_resum(request):

    resums = ResumCompany.objects.filter(is_active = True)
    return render(request,'partials/plus/resum.html',{'resums':resums})




def Show_Project(request):

    projects = ProjectModel.objects.filter(is_active = True).order_by('-created_at')
    return render(request,'partials/plus/project.html',{'projects':projects})





def show_decription(request):

    texts = text_description.objects.all()
    return render(request,'partials/plus/text.html',{'texts':texts})




def show_decription2(request):

    texts = text_description2.objects.all()
    return render(request,'partials/plus/text2.html',{'texts2':texts})




def show_metatag(request):

    metas = Meta_tag_model.objects.filter(is_active = True).first()
    return render(request,'partials/plus/meta.html',{'meta':metas})






def showComment(request):

    comments = Comment.objects.filter(isAvtive = True)
    return render(request,'partials/plus/comments.html',{'comments':comments})




def call(request):


    return render(request,'partials/plus/call.html')



def about(request):


    return render(request,'partials/plus/about.html')