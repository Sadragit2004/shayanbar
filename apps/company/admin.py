from django.contrib import admin
from django.utils.html import format_html
from .models import Comment,text_description,ProjectModel,ResumCompany,Company, MediaUrl, Slider_main, Meta_tag_model,WhyUs,text_description2


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'phone_number', 'email', 'is_active', 'create_at')
    search_fields = ('name_company', 'email')
    list_filter = ('is_active',)
    ordering = ('-create_at',)


@admin.register(MediaUrl)
class MediaUrlAdmin(admin.ModelAdmin):
    list_display = ('name_social', 'link', 'is_active', 'create_at')
    search_fields = ('name_social', 'link')
    list_filter = ('is_active',)



@admin.register(Slider_main)
class SliderMainAdmin(admin.ModelAdmin):
    list_display = ('id','image_name', 'is_active', 'create_at')
    list_filter = ('is_active',)
    ordering = ('-create_at',)



@admin.register(Meta_tag_model)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'page_title', 'index', 'created_at', 'updated_at')
    search_fields = ('site_name', 'page_title')
    list_filter = ('index',)
    ordering = ('-created_at',)


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'text')
    readonly_fields = ('image_tag',)


    def image_tag(self, obj):
        if obj.image_name:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:5px;" />', obj.image_name.url)
        return "-"
    image_tag.short_description = 'پیش‌ نمایش تصویر'



@admin.register(ResumCompany)
class ResumAdminCompany(admin.ModelAdmin):

    list_display = ('title','answer',)




@admin.register(ProjectModel)
class ProjectModeladmin(admin.ModelAdmin):

    list_display = ('title',)



@admin.register(text_description)
class text_Admin(admin.ModelAdmin):

    list_display = ('description',)


@admin.register(text_description2)
class text_Admin(admin.ModelAdmin):

    list_display = ('description',)


@admin.register(Comment)
class text_Admin(admin.ModelAdmin):

    list_display = ('fullName',)

