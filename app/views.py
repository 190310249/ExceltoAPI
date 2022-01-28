from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils.html import json_script
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import datetime
from .models import Customer, Excel, Branch, Home, Office, Loan
from .serializers import ExcelSerializer, CustomerSerializer, BranchSerializer, HomeSerializer, OfficeSerializer, LoanSerializer
import os
from django.conf import settings
import openpyxl
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
 
class index(View):
 def get(self, request):
  candidates = Excel.objects.last()
  return render(request, 'home.html', { 'candidates':candidates})
 def post(self, request):   
  name = request.POST.get('name')  
  pro=Excel(file=name)
  pro.save()
  excel = Excel.objects.last()
  excel1 = str(excel.file)
  base = str(BASE_DIR)
  data = ( base +'/media/documents/'+ excel1 )
  wb = openpyxl.load_workbook(data)
  sh1 = wb['Sheet1']
  id111=sh1['B2'].value
  cust1 = Customer.objects.filter(id=1)
  cust = Customer(name=sh1['A2'].value,father_name=sh1['A3'].value,profile=sh1['A4'].value,loan_acc_no=sh1['A5'].value)
  cust.save()
  br = Branch(customer=cust1[0],zone_name=sh1['B3'].value,region_name=sh1['B4'].value,branch_name=sh1['B5'].value,branch_code=sh1['B6'].value)
  br.save()
  hm = Home(customer=cust1[0],add_1=sh1['C3'].value,add_2=sh1['C4'].value,add_3=sh1['C5'].value,home_code=sh1['C6'].value,landmark=sh1['C7'].value)
  hm.save()
  ofi = Office(customer=cust1[0],add_1=sh1['D3'].value,add_2=sh1['D4'].value,add_3=sh1['D5'].value,off_code=sh1['D6'].value,landmark=sh1['D7'].value)
  ofi.save()
  loa = Loan(customer=cust1[0],agr_date=sh1['E3'].value,lrn=sh1['E4'].value,tenor=sh1['E5'].value,adv_emi=sh1['E6'].value,mob=sh1['E7'].value)
  loa.save()
  return render(request, 'home.html')



# For API Handeling

class excelapi(APIView):
    def post(self,request):
        serializer = ExcelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            excel = Excel.objects.last()
            excel1 = str(excel.file)
            base = str(BASE_DIR)
            data = ( base +'/media/'+ excel1 )
            wb = openpyxl.load_workbook(data)
            sh1 = wb['Sheet1']
            id111=sh1['B2'].value
            cust1 = Customer.objects.filter(id=id111)
            cust = Customer(name=sh1['A2'].value,father_name=sh1['A3'].value,profile=sh1['A4'].value,loan_acc_no=sh1['A5'].value)
            cust.save()
            br = Branch(customer=cust1[0],zone_name=sh1['B3'].value,region_name=sh1['B4'].value,branch_name=sh1['B5'].value,branch_code=sh1['B6'].value)
            br.save()
            hm = Home(customer=cust1[0],add_1=sh1['C3'].value,add_2=sh1['C4'].value,add_3=sh1['C5'].value,home_code=sh1['C6'].value,landmark=sh1['C7'].value)
            hm.save()
            ofi = Office(customer=cust1[0],add_1=sh1['D3'].value,add_2=sh1['D4'].value,add_3=sh1['D5'].value,off_code=sh1['D6'].value,landmark=sh1['D7'].value)
            ofi.save()
            loa = Loan(customer=cust1[0],agr_date=sh1['E3'].value,lrn=sh1['E4'].value,tenor=sh1['E5'].value,adv_emi=sh1['E6'].value,mob=sh1['E7'].value)
            loa.save()
            # SEND THE LATEST MODEL TO API  Customer, Excel, Branch, Home, Office, Loan         
            data5 = Customer.objects.all()
            serializer1 = CustomerSerializer(data5,many=True)
            #************
            data6 = Branch.objects.all()
            serializer2 = BranchSerializer(data6,many=True)
            #***********
            data7 = Home.objects.all()
            serializer3 = HomeSerializer(data7,many=True)
            #***********
            data8 = Office.objects.all()
            serializer4 = OfficeSerializer(data8,many=True)
            #**********
            data9 = Loan.objects.all()
            serializer5 = LoanSerializer(data9,many=True)
            #**********
            data4 = Excel.objects.all()
            serializer = ExcelSerializer(data4,many=True)
            return Response({'message':'Done','Excel':serializer.data,'Customer':serializer1.data,'Branch':serializer2.data,'Home':serializer3.data,'Office':serializer4.data,'Loan':serializer5.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Excel.objects.all()
        serializer = ExcelSerializer(data,many=True)
        return Response(serializer.data)

class Customerapi(APIView):
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Customer.objects.all()
            serializer = CustomerSerializer(data,many=True)
            return Response({'message':'Done','Customer':serializer.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Customer.objects.all()
        serializer = CustomerSerializer(data,many=True)
        return Response(serializer.data)


class Branchapi(APIView):
    def post(self,request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Branch.objects.all()
            serializer = BranchSerializer(data,many=True)
            return Response({'message':'Done','Branch':serializer.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Branch.objects.all()
        serializer = BranchSerializer(data,many=True)
        return Response(serializer.data)


class Homeapi(APIView):
    def post(self,request):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Home.objects.all()
            serializer = HomeSerializer(data,many=True)
            return Response({'message':'Done','Home':serializer.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Home.objects.all()
        serializer = HomeSerializer(data,many=True)
        return Response(serializer.data)


class Officeapi(APIView):
    def post(self,request):
        serializer = OfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Office.objects.all()
            serializer = OfficeSerializer(data,many=True)
            return Response({'message':'Done','Office':serializer.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Office.objects.all()
        serializer = OfficeSerializer(data,many=True)
        return Response(serializer.data)


class Loanapi(APIView):
    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Loan.objects.all()
            serializer = LoanSerializer(data,many=True)
            return Response({'message':'Done','Loan':serializer.data})
        return Response(serializer.errors)
    def get(self,request):
        data = Loan.objects.all()
        serializer = LoanSerializer(data,many=True)
        return Response(serializer.data)


# user = request.user
# 	add = Customer.objects.filter(user=user)

def test(request):
    user = request.user
    id=1
    data = Customer.objects.filter(id=id)
    print(data[0])
    return HttpResponse("Job Done")