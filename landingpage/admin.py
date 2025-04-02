from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Inline Admin for FactDetails


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'age', 'dob', 'address', 'city', 'profile_picture')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone_number', 'website')
        }),
        ('Profession', {
            'fields': ('bio', 'about_profession', 'profession', 'cover_profession', 'freelanceAvailability')
        }),
        ('Education', {
            'fields': ('degree',)
        }),
    )
    list_display = ('name', 'age', 'address', 'email', 'phone_number')

# for single profile form only

    # def changelist_view(self, request, extra_context=None):
    #     # Redirect to the change form of the first object
    #     first_object = Profile.objects.first()
    #     if first_object:
    #         return HttpResponseRedirect(reverse('admin:landingpage_profile_change', args=[first_object.id]))
    #     else:
    #         # If no objects exist, show the add form
    #         return HttpResponseRedirect(reverse('admin:landingpage_profile_add'))

    # def has_add_permission(self, request):
    #     # Prevent adding more than one object
    #     if Profile.objects.exists():
    #         return False
    #     return True

    # def has_delete_permission(self, request, obj=None):
    #     # Allow deletion only if there is more than one object
    #     if Profile.objects.count() > 1:
    #         return True
    #     return False


class WebsiteProfileAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        # Redirect to the change form of the first object
        first_object = WebsiteProfile.objects.first()
        if first_object:
            return HttpResponseRedirect(reverse('admin:landingpage_websiteprofile_change', args=[first_object.id]))
        else:
            # If no objects exist, show the add form
            return HttpResponseRedirect(reverse('admin:landingpage_websiteprofile_add'))

    def has_add_permission(self, request):
        # Prevent adding more than one object
        if WebsiteProfile.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deletion only if there is more than one object
        if WebsiteProfile.objects.count() > 1:
            return True
        return False


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # How many empty forms to display


class SkillHeadAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

    list_display = ('profile', 'description')
    search_fields = ('profile__name',)


class ExperienceInline(admin.StackedInline):  # or admin.StackedInline
    model = Experience
    extra = 1


class EducationInline(admin.StackedInline):  # or admin.StackedInline
    model = Education
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline, EducationInline]
    fieldsets = (
        ('Introduction', {
            'fields': ('profile', 'description')
        }),
    )


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1  # How many empty forms to display


class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

    list_display = ('profile', 'description')
    search_fields = ('name', 'description')


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1  # How many empty forms to display


class TestimonialsAdmin(admin.ModelAdmin):
    inlines = [TestimonialInline]

    list_display = ('profile', 'description')
    search_fields = ('name', 'description')


class PortfolioItemInline(admin.StackedInline):
    model = PortfolioItem
    extra = 1  # How many empty forms to display


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioItemInline]


admin.site.register(SkillHead, SkillHeadAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(WebsiteProfile, WebsiteProfileAdmin)
admin.site.register(Facts)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio, PortfolioAdmin)
