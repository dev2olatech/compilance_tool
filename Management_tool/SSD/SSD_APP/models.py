from django.db import models
from django import forms
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage



# Create your models here.


class Users(models.Model):
    """
     It will creat a table for the User
    """
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=100)
    department = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    id_type = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    id_expiry_date = models.DateField(null= True, blank = True)

    class Meta:
        db_table = 'Users'



class UPSI(models.Model):
    """
     It will creat a table for the UPSI.
     Managing a UPSI
    """
    Id = models.AutoField(primary_key=True)
    Nature = models.CharField(max_length=254, null=True)
    Purpose = models.CharField(max_length=254, null=True)
    Remark = models.CharField(max_length=500, null=True)
    Attachment1 = models.FileField(upload_to="")
    Attachment2 = models.FileField(upload_to="")

    def delete(self, filename, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.qr_code.name))
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'UPSI'


class DISCLOSURE(models.Model):
    """
    It will create a table format for stoare DISCLOSURE
    Information
    """
    Id = models.AutoField(primary_key=True)
    shared_by = models.CharField(max_length=254, null=True, blank= True)
    Nature_of_UPSI = models.CharField(max_length=254,null=True, blank= True)
    Purpose_of_sharing = models.CharField(max_length=254,null=True, blank= True)
    Remark = models.CharField(max_length=254,null=True, blank= True)
    shared_on = models.DateField()
    disc_Attachment = models.FileField(upload_to="")
    Recipients_name = models.CharField(max_length=100,null=True, blank= True)
    Recipients_email = models.EmailField(max_length=100,null=True, blank= True)
    Recipients_mobile_number = models.CharField(max_length=18,null=True, blank= True)
    Recipients_Id_Type = models.CharField(max_length=100,null=True, blank= True)
    Recipients_Id_Number = models.CharField(max_length=100,null=True, blank= True)

    def delete(self, filename, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.qr_code.name))
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'DISCLOSURE'
