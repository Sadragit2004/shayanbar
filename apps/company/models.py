from django.db import models
from django.utils import timezone
import funcs
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Company(models.Model):

    name_company = models.CharField(max_length=100,verbose_name='نام شرکت')
    phone_number = models.CharField(max_length=100,verbose_name='شماره موبایل',blank=True,null=True)
    mobile_number= models.CharField(max_length=100,verbose_name='شماره همراه ',blank=True,null=True)
    email = models.EmailField(verbose_name='ایمیل شرکت',blank=True,null=True)
    image_upload = funcs.FileUpload('Img','logo')
    image_name = models.FileField(upload_to=image_upload.upload_to,verbose_name='اپلود کردن عکس',
                                  validators=[funcs.validate_image_or_svg],blank=True,null=True)
    is_active = models.BooleanField(default=True,verbose_name='وضعیت')
    time_work = models.CharField(verbose_name='تایم کاری',max_length=100,blank=True,null=True)
    address = models.TextField(verbose_name='ادرس شرکت',blank=True,null=True)
    create_at = models.DateTimeField(verbose_name='ساخته شده',default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True,verbose_name='اپدیت کردن')
    video_uploader = funcs.FileUpload('video','company')
    video = models.FileField(upload_to=video_uploader.upload_to,verbose_name='ویدیو',blank=True,null=True)


    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات های شرکت'


    def __str__(self):
        return self.name_company




class MediaUrl(models.Model):

    name_social = models.CharField(max_length=100,verbose_name='نام مجازی')
    link = models.TextField(verbose_name='لینک')
    icon = models.TextField(verbose_name='ایکون',blank=True,null=True)
    is_active = models.BooleanField(default=True,verbose_name='وضعیت')
    create_at = models.DateTimeField(default=timezone.now,verbose_name='تاریخ ساخت')


    class Meta:

        verbose_name = 'شبکه اجتماعی '
        verbose_name_plural = 'شبکه اجتماعی های شرکت'


class Slider_main(models.Model):


    title = models.CharField(max_length=100,verbose_name='عنوان',blank=True,null=True)
    text = models.TextField(blank=True,null=True,verbose_name='متن')
    image_file = funcs.FileUpload('Img','slider_main')
    image_name = models.ImageField(verbose_name='نام تصویر',upload_to=image_file.upload_to)
    alt = models.CharField(max_length=100,verbose_name='متن جایگزین ',blank=True,null=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    create_at = models.DateTimeField(verbose_name='تاریخ ثبت',default=timezone.now)



    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس های اسلایدر'



class Meta_tag_model(models.Model):

    site_name = models.CharField(max_length=255, null=True, blank=True)  # عنوان صفحه
    page_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان صفحه
    description = models.TextField(null=True, blank=True)  # توضیحات، حداکثر 128 کاراکتر
    og_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان OG
    og_description = models.TextField(null=True, blank=True)  # توضیحات OG
    alt = models.CharField(null=True, blank=True,max_length=100)  # تصویر OG (URL)
    og_image = models.URLField(null=True, blank=True)  # تصویر OG (URL)

    # این فیلد برای مدیریت ساختار og (Open Graph)
    og_url = models.URLField(null=True, blank=True)  # URL برای OG
    og_type = models.CharField(max_length=50, null=True, blank=True)
    index = models.BooleanField(verbose_name='ایندکس',default=True)
    # برای تعیین تاریخ و زمان ایجاد و آپدیت
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True,verbose_name='متا تگ')


    def __str__(self):
        return self.site_name



    class Meta:

        verbose_name = 'تگ مدل'
        verbose_name_plural = 'تگ های متا صفحه اصلی'


    def save(self, *args, **kwargs):
        # اگر توضیحات بیش از 128 کاراکتر باشد، آنها را کوتاه می‌کنیم
        if self.description and len(self.description) > 150:
            self.description = self.description[:150]
        super(Meta_tag_model, self).save(*args, **kwargs)



class WhyUs(models.Model):

    image_file = funcs.FileUpload('Img','whyus')
    image_name = models.FileField(verbose_name='نام تصویر',upload_to=image_file.upload_to,validators=[funcs.validate_image_or_svg])
    title = models.CharField(max_length=100,verbose_name='متن')
    text = models.TextField(verbose_name='متن')
    is_active = models.BooleanField(default=True,verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:

        verbose_name = 'چرا ما'
        verbose_name_plural = 'چرا ما ؟ '





class ResumCompany(models.Model):

    title = models.CharField(max_length=30,verbose_name='موضوع')
    answer = models.CharField(max_length=20,verbose_name='جواب رزوم')
    is_active = models.BooleanField(default=True,)



    def __str__(self):
        return self.title


    class Meta:

        verbose_name = 'رزومه سایت'
        verbose_name_plural = 'رزومه های سایت'




class ProjectModel(models.Model):

    title = models.CharField(max_length=100,verbose_name='موضوع')
    image_file = funcs.FileUpload('Img','project')
    image_name = models.FileField(verbose_name='نام تصویر',upload_to=image_file.upload_to,validators=[funcs.validate_image_or_svg])
    is_active = models.BooleanField(default=True,verbose_name='وضعیت')
    created_at = models.DateTimeField(default=timezone.now,verbose_name='ثبت شده')


    def __str__(self):
        return self.title



    class Meta:

        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'



class text_description(models.Model):


    image_file = funcs.FileUpload('Img','project')
    image_name = models.FileField(verbose_name='نام تصویر',upload_to=image_file.upload_to,validators=[funcs.validate_image_or_svg],blank=True,null=True)
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    title = models.CharField(max_length=40,verbose_name='عنوان توضیحات',blank=True,null=True)



class text_description2(models.Model):


    image_file = funcs.FileUpload('Img','project')
    image_name = models.FileField(verbose_name='نام تصویر',upload_to=image_file.upload_to,validators=[funcs.validate_image_or_svg],blank=True,null=True)
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    title = models.CharField(max_length=40,verbose_name='عنوان توضیحات',blank=True,null=True)



    class Meta:

        verbose_name = 'متن پایین'
        verbose_name_plural = 'متن پایین تصویر'





class Comment(models.Model):

    fullName = models.CharField(max_length=100,verbose_name='نام کامل')
    semat = models.CharField(max_length=100,verbose_name='سمت')
    text = models.TextField(verbose_name='متن پیام')
    isAvtive = models.BooleanField(default=True)