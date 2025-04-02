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
        website_profile_id = WebsiteProfile.objects.first().profile.id
        if website_profile_id:
            profile = Profile.objects.filter(
                id=website_profile_id).first()
        if profile:
            facts = Facts.objects.filter(profile=profile).first()
            skill_head = SkillHead.objects.filter(profile=profile).first()
            skills = skill_head.list_of_skills.all()
            resume = Resume.objects.filter(profile=profile).first()
            educations = Education.objects.filter(resume=resume).all()
            experiences = Experience.objects.filter(resume=resume).all()
            services = Services.objects.filter(profile=profile).first()
            testimonials = Testimonials.objects.filter(profile=profile).first()
            contact = Contact.objects.filter(profile=profile).first()
            portfolio = Portfolio.objects.filter(profile=profile).first()
            portfolio_categories = PortfolioCategory.objects
            page_context = {
                'profile': profile,
                'facts': facts,
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
