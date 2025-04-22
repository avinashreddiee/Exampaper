
from django.db import models


class superintendent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


class teachers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    work_exp = models.CharField(max_length=1000)
    work_address = models.CharField(max_length=100)
    

class paper_request(models.Model):
    examid = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=15, blank=True, null=True)
    stz = models.CharField(max_length=100)
    paper = models.CharField(max_length=100)

class alloted_teachers(models.Model):
    eid = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=15, blank=True, null=True)
    teacher_email=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    stz = models.CharField(max_length=100)
    pdf = models.CharField(max_length=100)
    

class recipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100)
    organization = models.CharField(max_length=1000)
    org_address = models.CharField(max_length=100)


