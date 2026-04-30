from django.urls import path
from .views import about,call,showComment,show_decription2,show_metatag,show_mobile_number,show_name,show_decription,Show_Project,show_resum,WhyUsBox,SociaMediaview,show_phone_number,show_address,time_work,show_logo,sliders

app_name = 'company'

urlpatterns = [

   path('phone-number/',show_phone_number,name='phone_number'),
   path('monile-number/',show_mobile_number,name='mobile_number'),
   path('address',show_address,name='address'),
   path('time_work/',time_work,name='time'),
   path('show-logo/',show_logo,name='logo'),
   path('sliders/',sliders,name='sliders'),
   path('social_media/',SociaMediaview,name='social'),
   path('whys/',WhyUsBox,name='why'),
   path('resum/',show_resum,name='resum'),
   path('show-project/',Show_Project,name='project'),
   path('text/',show_decription,name='text'),
   path('text2/',show_decription2,name='text2'),
   path('name/',show_name,name='name'),
   path('showComment/',showComment,name='comment'),
   path('metas/',show_metatag,name='meta'),
   path('call/',call,name='callview'),
   path('abouts',about,name='about'),


]
