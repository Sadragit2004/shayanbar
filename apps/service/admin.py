from django.contrib import admin
from .models import GalleryService,Feature,Meta_tag_model_group,faq,Service, Item, Plan, PlanItem,Groups,Meta_tag_model


# Inline configuration for Item (TabularInline)
class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    verbose_name = 'آیتم'
    verbose_name_plural = 'آیتم‌ها'



class GalleryServiceInline(admin.TabularInline):

    model = GalleryService
    extra = 1



class FeatureInline(admin.TabularInline):

    model = Feature
    extra = 1


class MetaTagGroupAdminTabular(admin.TabularInline):

    model = Meta_tag_model_group
    extra = 1




class planInlineTabular(admin.TabularInline):

    model = Plan
    extra = 1



class FaqTabularInline(admin.TabularInline):
    model = faq
    extra = 1


# Admin configuration for Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    inlines = [GalleryServiceInline,ItemInline,planInlineTabular,FaqTabularInline,FeatureInline]  # TabularInline for Item
    verbose_name = 'سرویس'
    verbose_name_plural = 'سرویس‌ها'


# Inline configuration for PlanItem (TabularInline)
class PlanItemInline(admin.TabularInline):
    model = PlanItem
    extra = 1
    verbose_name = 'آیتم پلن'
    verbose_name_plural = 'آیتم‌های پلن'


# Admin configuration for Plan
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'price')
    inlines = [PlanItemInline]  # TabularInline for PlanItem
    verbose_name = 'پلن'
    verbose_name_plural = 'پلن‌ها'


# Admin configuration for Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    verbose_name = 'آیتم'
    verbose_name_plural = 'آیتم‌ها'


# Admin configuration for PlanItem
@admin.register(PlanItem)
class PlanItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan', 'is_checked', 'created_at', 'update_at')
    list_filter = ('is_checked', 'created_at')
    search_fields = ('title',)
    verbose_name = 'آیتم پلن'
    verbose_name_plural = 'آیتم‌های پلن'



@admin.register(Groups)
class GroupsServiceAdmin(admin.ModelAdmin):

    list_display = ('title_group',)
    inlines= [MetaTagGroupAdminTabular]





@admin.register(Meta_tag_model)
class MetaAdmin(admin.ModelAdmin):

    list_display = ('page_title','service',)