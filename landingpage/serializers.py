from rest_framework import serializers
from .models import Message


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['full_name', 'email', 'subject', 'message']
