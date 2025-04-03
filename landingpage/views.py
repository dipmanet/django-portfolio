from .models import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessagesSerializer


class LandingPageView(APIView):
    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        website_profile = WebsiteProfile.objects.first()
        profile = Profile.objects.first()

        if website_profile:
            profile = Profile.objects.filter(
                id=website_profile.profile.id).first()

        if profile:
            facts = Facts.objects.filter(profile=profile).first()
            skill_head = SkillHead.objects.filter(profile=profile).first()
            skills = skill_head.list_of_skills.all() if skill_head else []

            resume = Resume.objects.filter(profile=profile).first()
            educations = Education.objects.filter(resume=resume).all()
            experiences = Experience.objects.filter(resume=resume).all()

            services = Services.objects.filter(profile=profile).first()
            testimonials = Testimonials.objects.filter(profile=profile).first()
            contact = Contact.objects.filter(profile=profile).first()
            portfolio = Portfolio.objects.filter(profile=profile).first()
            portfolio_categories = PortfolioCategory.objects.all()

            page_context = {
                'profile': profile,
                'facts': facts or "No facts available.",
                'skill_head': skill_head,
                'skills': skills,
                'resume': resume,
                'educations': educations,
                'experiences': experiences,
                'services': services,
                'testimonials': testimonials,
                'contact': contact,
                'portfolio': portfolio,
                'portfolio_categories': portfolio_categories,
            }
            return render(request, 'index.html', context=page_context)

        else:
            return render(request, 'empty_state.html')
