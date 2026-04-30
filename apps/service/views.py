from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Service,Groups,Meta_tag_model,Meta_tag_model_group
# Create your views here.

class ServicelistView(View):
    def get(self,request,*args, **kwargs):

        services = Service.objects.filter(is_active = True).order_by('-created_at')[:6]
        return render(request,'service_app/service_main.html',{'services':services})



class DetailServiceView(View):

    def get(self, request, *args, **kwargs):

        slug = kwargs.get('slug')


        service = get_object_or_404(Service, slug=slug)

        metas = Meta_tag_model.objects.filter(service=service).first()
        return render(request, 'service_app/service_detail.html', {'service': service, 'meta': metas})




def show_title_service(request):
    services = Service.objects.filter(is_active = True).order_by('-created_at')[:4]
    return render(request,'service_app/service_title.html',{'services':services})



def show_group(request):

    groups = Groups.objects.filter(is_active = True).order_by('-created_at')


    return render(request,'service_app/show_group.html',{'groups':groups})



def show_by_group(request,*args, **kwargs):

    slug = kwargs['slug']
    groups = Groups.objects.filter(slug = slug).first()
    services = Service.objects.filter(groups = groups)

    metas = Meta_tag_model_group.objects.filter(group = groups).first()

    return render(request,'service_app/show_by_group.html',{'services':services,'group_name':groups.title_group,'meta':metas})



class ServiceListOrgPage(View):
    def get(self,request,*args, **kwargs):


        slug = kwargs.get('slug')

        if slug:
                group = Groups.objects.filter(slug = slug).first()
                service = Service.objects.filter(is_active = True,groups = group).order_by('-created_at')
                metas = Meta_tag_model_group.objects.filter(group = group).first()
                return render(request,'service_app/service_list.html',{'services':service,'group':group,'meta':metas})


        else:
            group = Groups.objects.filter(slug = slug).first()
            service = Service.objects.filter(is_active = True).order_by('-created_at')
            metas = Meta_tag_model_group.objects.filter(group = group).first()
            return render(request,'service_app/service_list.html',{'services':service,"meta":metas})



def show_group_header(request):

    groups = Groups.objects.filter(is_active = True).order_by('-created_at')


    return render(request,'service_app/show_group_header.html',{'groups':groups})


