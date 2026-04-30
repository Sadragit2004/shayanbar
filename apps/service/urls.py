from django.urls import path,include
from .views import show_group_header,show_by_group,show_group,ServicelistView,show_title_service,ServiceListOrgPage,DetailServiceView

app_name = 'project'

urlpatterns = [
    path('servicesview/', ServicelistView.as_view(), name='services'),
    path('service-title/', show_title_service, name='titles'),
    path('service/', ServiceListOrgPage.as_view(), name='service'),
    path('show_group/', show_group, name='groups'),
    path('header-group/', show_group_header, name='group-header'),

    # آخرین مسیر باشد
    path('<str:slug>', DetailServiceView.as_view(), name='servicedetail'),
]

