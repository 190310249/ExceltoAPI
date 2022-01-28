from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Excel, Branch, Home, Office, Loan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Excel
        fields="__all__"

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields="__all__"


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields="__all__"

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Office
        fields="__all__"

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields="__all__"