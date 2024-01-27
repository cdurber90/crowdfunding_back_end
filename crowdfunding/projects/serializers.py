from rest_framework import serializers
from .models import HealthcareHero, Donation

class HealthcareHeroSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = HealthcareHero
        fields = "__all__"

class DonationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.healthcarehero = validated_data.get('Healthcare Hero', instance.healthcarehero)
        instance.save()
        return instance
    
    class Meta:
        model = Donation
        fields ='__all__'

class HealthcareHeroDetailSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance





class DonationDetailSerializer(serializers.ModelSerializer):
    healthcarehero = HealthcareHeroSerializer(many=True, read_only=True)
    donation = DonationSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        instance.ticket_name = validated_data.get('ticket_name', instance.ticket_name)
        instance.cost = validated_data.get('cost',instance.cost)
        instance.features = validated_data.get('features', instance.features)
        instance.festival = validated_data.get('festival', instance.festival)
        instance.ticket_owner = validated_data.get('ticket_owner', instance.ticket_owner)
        instance.save()
        return instance
    
    class Meta:
        model = Donation
        fields = "__all__"
    





