from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import funcs
import jdatetime
# Create your models here.


class Groups(models.Model):

    title_group = models.CharField(max_length=100,verbose_name='عنوان گروه')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )
    slug = models.CharField(max_length=100,verbose_name='نامک',null=True,blank=True)


    class Meta:

        verbose_name = 'گروه خدمات'
        verbose_name_plural = 'گروه های خدمات'


    def __str__(self):
        return self.title_group




class Meta_tag_model_group(models.Model):


    group = models.ForeignKey(Groups,on_delete=models.CASCADE,verbose_name='گروه خدمات')
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

    def __str__(self):
        return self.site_name



class Service(models.Model):

    title = models.CharField(max_length=100,verbose_name='نام سرویس',blank=True,null=True)
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    text_summery = models.TextField(verbose_name='متن خلاصه',blank=True,null=True)
    image_file = funcs.FileUpload('images','service')
    groups = models.ForeignKey(Groups,on_delete=models.CASCADE,verbose_name='گروه ها',null=True,blank=True)
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='نام فایل')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )
    svg_file = models.TextField(verbose_name='svg ',blank=True,null=True)


    slug = models.CharField(max_length=100,verbose_name='نامک',null=True,blank=True)
    city  = models.TextField(verbose_name='شهر',blank=True,null=True)

    def __str__(self):
        return f'{self.title}'


    def get_jalali_register_date(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d')


    class Meta:

        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'


class Item(models.Model):

    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='سرویس',related_name='item_services')
    title = models.CharField(max_length=100,verbose_name='موضوع')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )

    def __str__(self):
        return f'{self.title}'



    class Meta:

        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها ایتم'





class Plan(models.Model):


    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='سرویس ها',related_name='plan_service',blank=True,null=True)
    title = models.CharField(max_length=100,verbose_name='موضوع پلن',blank=True,null=True)
    price = models.PositiveIntegerField(verbose_name='قیمت',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )

    image_file = funcs.FileUpload('images','service')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='نام فایل',blank=True,null=True)


    def __str__(self):
        return f'{self.title}\t\t{self.price}'


    class Meta:

        verbose_name = 'پلن '
        verbose_name_plural = 'پلن ها'



class PlanItem(models.Model):

    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,verbose_name='پلن',related_name='plan_item')
    title = models.CharField(verbose_name='عنوان',max_length=100,null=True,blank=True)
    is_checked = models.BooleanField(default=True,verbose_name='check')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )


    def __str__(self):
        return f'{self.title}'


class Meta_tag_model(models.Model):

    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='خدمات',blank=True,null=True)
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

    def __str__(self):
        return self.page_title or 'Meta Tag for {}'.format(self.service)


    class Meta:

        verbose_name = 'متا تگ های بلاگ'
        verbose_name_plural = 'متا تگ های وبلاگ'


    def save(self, *args, **kwargs):
        # اگر توضیحات بیش از 128 کاراکتر باشد، آنها را کوتاه می‌کنیم
        if self.description and len(self.description) > 150:
            self.description = self.description[:150]
        super(Meta_tag_model, self).save(*args, **kwargs)



class faq(models.Model):


    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='وبلاگ',related_name='services_faqs',null=True,blank=True)
    question = models.CharField(max_length=300,verbose_name='سوال',null=True,blank=True)
    answer = models.TextField(verbose_name='جواب',null=True,blank=True)
    is_active = models.BooleanField(verbose_name='وضعیت',default=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ',null=True,blank=True)


    def __str__(self) -> str:
        return f'{self.question}'


    class Meta:

        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات'




class Feature(models.Model):

    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='خدمات',related_name='serivce_feature')
    title = models.CharField(max_length=100,verbose_name='کلمه')
    value = models.CharField(max_length=100,verbose_name='مقدار')
    is_active  = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.title}"




class GalleryService(models.Model):


    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='عکس ها',related_name='gallery_service')
    alt = models.CharField(max_length=100,verbose_name='متن جایگزین',blank=True,null=True)
    image_file = funcs.FileUpload('images','gallery_service')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='عکس')
    is_active = models.BooleanField(default=True,verbose_name='وضعیت فعال')
    create_at = models.DateTimeField(default=timezone.now,verbose_name='تاریخ ساخته شده')

    def __str__(self):
        return f'{self.alt}\t{self.create_at}'


    class Meta:

        verbose_name = 'عکس'
        verbose_name_plural = 'گالری خدمات'