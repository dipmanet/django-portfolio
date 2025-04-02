from django.db import models
from datetime import date
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Profile(models.Model):
    name = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True, unique=True)
    address = models.CharField(max_length=50, null=True)
    dob = models.DateField(default=date.today)
    website = models.URLField(null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True)
    city = models.CharField(max_length=30, null=True)
    degree = models.CharField(null=True, max_length=30, blank=True)

    profile_picture = models.ImageField(
        upload_to="images/", null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    freelanceAvailability = models.BooleanField(default=False)
    profession = models.CharField(max_length=30, null=True)
    cover_profession = models.CharField(max_length=30, null=False, blank=True)
    about_profession = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Profile"


class WebsiteProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.profile.name}'s profile"

    def save(self, *args, **kwargs):
        if not self.pk and WebsiteProfile.objects.exists():
            raise ValidationError(
                'There can be only one WebsiteProfile instance')
        return super(WebsiteProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Website Profile"


class Facts(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=300, null=True, blank=True)
    number_happy_clients = models.IntegerField(default=0)
    number_projects = models.IntegerField(default=0)
    number_hours_of_support = models.IntegerField(default=0)
    number_hard_workers = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Facts for {self.profile.name}"

    class Meta:
        verbose_name_plural = "Facts"


class SkillHead(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=300, null=True)

    def __str__(self) -> str:
        return f"{self.profile.name}'s skills"

    class Meta:
        verbose_name_plural = "SkillHeads"


class Skill(models.Model):
    skill_head = models.ForeignKey(
        SkillHead, on_delete=models.CASCADE, default=1, related_name='list_of_skills')
    title = models.CharField(max_length=30, null=False, blank=False)
    percent = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id and self.order == 0:
            # Get the highest order value within the same SkillHead
            max_order = Skill.objects.filter(skill_head=self.skill_head).aggregate(
                models.Max('order')
            )['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.skill_head.profile.name}'s skill"

    class Meta:
        verbose_name_plural = "Skills"


class Resume(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=1)
    description = CKEditor5Field()

    def __str__(self) -> str:
        return f"{self.profile.name}'s Resume"

    class Meta:
        verbose_name_plural = "Resume"


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    level = models.CharField(max_length=50, null=False, blank=False)
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=True)
    institute = models.CharField(max_length=30, null=False, blank=False)
    university = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=400, null=True)

    def __str__(self) -> str:
        return f"{self.resume.profile.name}"

    class Meta:
        verbose_name_plural = "Education"


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    position = models.CharField(max_length=30, null=False)
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=30, null=True)
    responsibilities = models.TextField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.resume.profile.name}"

    class Meta:
        verbose_name_plural = "Experience"


class Services(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=300, null=True)

    def __str__(self) -> str:
        return f"{self.profile.name}'s services"

    class Meta:
        verbose_name_plural = "Services"


class Service(models.Model):
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, default=1, related_name='list_of_services')
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.service}"


class Testimonials(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, default=1)
    # profile = models.ForeignKey(
    #     Profile, on_delete=models.CASCADE, default=1, unique=True)

    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.profile.name}'s Testimonials"

    class Meta:
        verbose_name_plural = "Testimonials"


class Testimonial(models.Model):
    testimonial = models.ForeignKey(
        Testimonials, on_delete=models.CASCADE, default=1, related_name='list_of_testimonials')
    submitted_by = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.testimonial}"


class Contact(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=300, null=True)
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=30, null=True)

    def __str__(self) -> str:
        return f"{self.profile.name}"

    class Meta:
        verbose_name_plural = "Contact"


class Message (models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, default=1)
    full_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    subject = models.CharField(max_length=30, null=True)
    message = models.TextField(max_length=300, null=True)

    def __str__(self) -> str:
        return f"{self.subject}"


class PortfolioCategory (models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Portfolio Categories"


class Portfolio (models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, null=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.profile.name}'s portfolio"


class PortfolioItem (models.Model):
    slug = models.SlugField(null=True, unique=True, blank=True)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, default=1, related_name='list_of_portfolio_items')
    portfolio_category = models.ForeignKey(
        PortfolioCategory, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    link = models.URLField(max_length=30, null=True, blank=True)
    photos = models.ImageField(null=True, blank=True)

    project_category = models.CharField(max_length=30, null=True)
    project_client = models.CharField(max_length=30, null=True)
    project_date = models.CharField(max_length=30, null=True)
    project_url = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
