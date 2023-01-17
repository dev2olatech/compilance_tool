from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotModified
from SSD_APP.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.core.exceptions import BadRequest
from django.http import FileResponse
from django.conf import settings
import os
import json


# Create your views here.

def registerPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +  user )
            return redirect('home')
    context={'form': form}
    return render(request,'SSD_APP/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context={}
    return render(request,'SSD_APP/login.html',context)
    

def logoutUser(request):
    logout(request)
    return redirect('login')


###############################################################################################


@login_required(login_url='login')
def home(request):
    return render(request, 'SSD_APP/new_navbar.html')


def Users_View(request):
    """
    It is view function to show the list of Users which is present
    """
    user = Users.objects.all()

    if request.method == "GET":
        q = request.GET.get('searchname')
        if q != None:
            user = Users.objects.filter(name__icontains=q)

    context = {
        'user': user,
    }
    return render(request, 'SSD_APP/manage_user.html', context)


def user_addition(request):
    """
    It is view function for the additon of new users 
    """

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        department = request.POST.get('department')
        password = request.POST.get('password')
        role = request.POST.get('role')
        id_type = request.POST.get('id_type')
        id_number = request.POST.get('id_number')
        id_expiry_date = request.POST.get('id_expiry_date')


        user = Users(
            name = name,
            email = email,
            mobile_no = mobile_no,
            department = department,
            password = password,
            role = role,
            id_type = id_type,
            id_number = id_number,
            id_expiry_date = id_expiry_date,
        )


        user.save()
        return redirect('manage_users')
    return render(request, 'SSD_APP/add_user.html')


def user_edit(request, id):
    user = Users.objects.filter(Id = id)

    context = {
        'user': user,
    }
    return render(request, 'SSD_APP/edit_user.html', context)


    
def user_update(request, id):
    """
    It is view function for the additon of new users 
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        department = request.POST.get('department')
        password = request.POST.get('password')
        role = request.POST.get('role')
        id_type = request.POST.get('id_type')
        id_number = request.POST.get('id_number')
        id_expiry_date = request.POST.get('id_expiry_date')

        user = Users(
            Id = id,
            name = name,
            email = email,
            mobile_no = mobile_no,
            department = department,
            password = password,
            role = role,
            id_type = id_type,
            id_number = id_number,
            id_expiry_date = id_expiry_date
        )

        user.save()
        return redirect('manage_users')
    return render(request, 'SSD_APP/edit_user.html')



###############################################################################################

def Make_Disclosure(request):
    """
    It is view function to show the list of Users which is present
    """
    disclosure = DISCLOSURE.objects.all()
    for entry in disclosure:
        if entry.disc_Attachment == 'annonymous.pdf':
            entry.disc_Attachment = 'No File'


    if request.method == "GET":
        q = request.GET.get('searchnature')
        if q != None:
            disclosure = DISCLOSURE.objects.filter(Nature__icontains=q)
    context = {
        'disclosure': disclosure,
    }
    return render(request, 'SSD_APP/make_disclosure.html', context)


def disclosure_addition(request):
    """
    It is view function for the additon of new users
    """
    if request.method == "POST":
        shared_by = request.POST.get('shared_by')
        Nature_of_UPSI = request.POST.get('Nature_of_UPSI')
        Purpose_of_sharing = request.POST.get('Purpose_of_sharing')
        Remark= request.POST.get('Remark')
        shared_on = request.POST.get('shared_on')
        R_name = request.POST.get('R_name')
        R_email = request.POST.get('R_email')
        R_mobile = request.POST.get('R_mobile')
        R_id_type = request.POST.get('R_id_type')
        R_id_number = request.POST.get('R_id_number')
        try:
            Attachment = request.FILES['disc_Attachment']
        except:
            Attachment = 'annonymous.pdf'

        disclosure = DISCLOSURE(
            shared_by = shared_by,
            Nature_of_UPSI = Nature_of_UPSI,
            Purpose_of_sharing = Purpose_of_sharing,
            Remark = Remark,
            shared_on =shared_on,
            disc_Attachment = Attachment,
            Recipients_name = R_name,
            Recipients_email = R_email,
            Recipients_mobile_number = R_mobile,
            Recipients_Id_Type = R_id_type,
            Recipients_Id_Number = R_id_number
        )
        disclosure.save()
        return redirect('make_disclosure')
    return render(request, 'SSD_APP/add_report.html')


def disclosure_edit(request, id):
    disclosure = DISCLOSURE.objects.filter(Id = id).first
    context = {
        'disclosure': disclosure,
    }
    return render(request, 'SSD_APP/edit_report.html', context)

    
def disclosure_update(request, id):
    """
    It is view function for the additon of new users
    """
    if request.method == "POST":
        discl = DISCLOSURE.objects.filter(Id = id).first()
        attachment_name = request.POST.get('disc_Attachment')
        if discl.disc_Attachment == attachment_name:
            shared_by = request.POST.get(' shared_by')
            Nature_of_UPSI = request.POST.get('Nature_of_UPSI')
            Purpose_of_sharing = request.POST.get('Purpose_of_sharing')
            Remark= request.POST.get('Remark')
            shared_on = request.POST.get('shared_on')
            R_name = request.POST.get('R_name')
            R_email = request.POST.get('R_email')
            R_mobile = request.POST.get('R_mobile')
            R_id_type = request.POST.get('R_id_type')
            R_id_number = request.POST.get('R_id_number')

            disclosure = DISCLOSURE(
                Id = id,
                shared_by = shared_by,
                Nature_of_UPSI = Nature_of_UPSI,
                Purpose_of_sharing = Purpose_of_sharing,
                Remark = Remark,
                shared_on =shared_on,
                disc_Attachment = attachment_name,
             # disc_Attachment = Attachment,
                Recipients_name = R_name,
                Recipients_email = R_email,
                Recipients_mobile_number = R_mobile,
                Recipients_Id_Type = R_id_type,
                Recipients_Id_Number = R_id_number
            )
            disclosure.save()
            return redirect('make_disclosure')
        else:
            shared_by = request.POST.get('shared_by')
            Nature_of_UPSI = request.POST.get('Nature_of_UPSI')
            Purpose_of_sharing = request.POST.get('Purpose_of_sharing')
            Remark= request.POST.get('Remark')
            shared_on = request.POST.get('shared_on')
            R_name = request.POST.get('R_name')
            R_email = request.POST.get('R_email')
            R_mobile = request.POST.get('R_mobile')
            R_id_type = request.POST.get('R_id_type')
            R_id_number = request.POST.get('R_id_number')
            try:
                Attachment = request.FILES['disc_Attachment']
            except:
                Attachment = 'annonymous.pdf'

            disclosure = DISCLOSURE (
                Id = id,
                shared_by = shared_by,
                Nature_of_UPSI = Nature_of_UPSI,
                Purpose_of_sharing = Purpose_of_sharing,
                Remark = Remark,
                shared_on =shared_on,
                disc_Attachment = Attachment,
                Recipients_name = R_name,
                Recipients_email = R_email,
                Recipients_mobile_number = R_mobile,
                Recipients_Id_Type = R_id_type,
                Recipients_Id_Number = R_id_number
            )
            disclosure.save()
            return redirect('make_disclosure')
    return render(request, 'SSD_APP/edit_report.html')

def DeleteDisclosureAttachedPDF(request):
    id = request.GET['id']
    disclosure = DISCLOSURE.objects.filter(Id = id).first()
    file_to_delete = str(disclosure.disc_Attachment)
    media_path = settings.MEDIA_ROOT
    file_path = os.path.join(media_path, file_to_delete)
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        return HttpResponse(request, 'SSD_APP/edit_report.html')
    else:
        return HttpResponse(request, 'SSD_APP/edit_report.html')



##############################################################################################
def UPSI_View(request):
    """
    It is view function to show the list of UPSI which is present
    """
    upsi = UPSI.objects.all()
    for entry in upsi:
        if entry.Attachment1 == 'annonymous.pdf':
            entry.Attachment1 = 'No File'
        if entry.Attachment2 == 'annonymous.pdf':
            entry.Attachment2 = 'No File'

    if request.method == "GET":
        q = request.GET.get('searchnature')
        if q != None:
            upsi = UPSI.objects.filter(Nature__icontains=q)

    context = {
        'upsi': upsi,
    }
    return render(request, 'SSD_APP/manage_upsi.html', context)


def upsi_addition(request):
    """
    It is view function for the additon of new users
    """
    if request.method == "POST":
        Nature = request.POST.get('Nature')
        Purpose = request.POST.get('Purpose')
        Remark = request.POST.get('Remark')
        try:
            Attachment1 = request.FILES['Attachment1']
        except:
            Attachment1 = 'annonymous.pdf'
        
        try:
            Attachment2 = request.FILES['Attachment2']
        except:
            Attachment2 = 'annonymous.pdf'

        upsi = UPSI (
            Nature = Nature,
            Purpose = Purpose,
            Remark = Remark,
            Attachment1 = Attachment1,
            Attachment2 = Attachment2,
        )
        upsi.save()
        return redirect('manage_upsi')
    return render(request, 'SSD_APP/add_upsi.html')


def upsi_edit(request, id):
    upsi = UPSI.objects.filter(Id = id).first
    
    context = {
        'upsi' : upsi,
    }
    return render(request, 'SSD_APP/edit_upsi.html', context)

def upsi_update(request, id):
    """
    It is view function for the additon of new Upsi 
    """
    if request.method == "POST":
        upsi = UPSI.objects.filter(Id = id).first()
        attachment_name1 = request.POST.get('Attachment1')
        attachment_name2 = request.POST.get('Attachment2')
        if upsi.Attachment1 == attachment_name1 and upsi.Attachment2 == attachment_name2 :
            Nature = request.POST.get('Nature')
            Purpose = request.POST.get('Purpose')
            Remark = request.POST.get('Remark')
            upsi = UPSI (
                Id = id,
                Nature = Nature,
                Purpose = Purpose,
                Remark = Remark,
                Attachment1 = attachment_name1,
                Attachment2 = attachment_name2
            )
            upsi.save()
            return redirect('manage_upsi')

        elif upsi.Attachment1 != attachment_name1 and upsi.Attachment2 == attachment_name2 :
            try:
                Attachment1 = request.FILES['Attachment1']
            except:
                Attachment1 = 'annonymous.pdf'
            Nature = request.POST.get('Nature')
            Purpose = request.POST.get('Purpose')
            Remark = request.POST.get('Remark')
            upsi = UPSI (
                Id = id,
                Nature = Nature,
                Purpose = Purpose,
                Remark = Remark,
                Attachment1 = Attachment1,
                Attachment2 = attachment_name2
            )
            upsi.save()
            return redirect('manage_upsi')

        elif upsi.Attachment1 == attachment_name1 and upsi.Attachment2 != attachment_name2 :
            try:
                Attachment2 = request.FILES['Attachment2']
            except:
                Attachment2 = 'annonymous.pdf'
            Nature = request.POST.get('Nature')
            Purpose = request.POST.get('Purpose')
            Remark = request.POST.get('Remark')
            upsi = UPSI (
                Id = id,
                Nature = Nature,
                Purpose = Purpose,
                Remark = Remark,
                Attachment1 = attachment_name1,
                Attachment2 = Attachment2
            )
            upsi.save()
            return redirect('manage_upsi')
        else:
            Nature = request.POST.get('Nature')
            Purpose = request.POST.get('Purpose')
            Remark = request.POST.get('Remark')
            try:
                Attachment1 = request.FILES['Attachment1']
            except:
                Attachment1 = 'annonymous.pdf'
            try:
                Attachment2 = request.FILES['Attachment2']
            except:
                Attachment2 = 'annonymous.pdf'
            upsi = UPSI (
                Id = id,
                Nature = Nature,
                Purpose = Purpose,
                Remark = Remark,
                Attachment1 = Attachment1,
                Attachment2 = Attachment2
            )
            upsi.save()
            return redirect('manage_upsi')
    return render(request, 'SSD_APP/edit_upsi.html')

def DeleteAttachedPDF1(request):
    id = request.GET['id']
    upsi = UPSI.objects.filter(Id = id).first()
    print(upsi.Attachment1)
    file = str(upsi.Attachment1)
    media_path = settings.MEDIA_ROOT
    file_path = os.path.join(media_path, file)
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        return HttpResponse(request, 'SSD_APP/edit_upsi.html')
    else:
        return HttpResponse(request, 'SSD_APP/edit_upsi.html')

def DeleteAttachedPDF2(request):
    id = request.GET['id']
    upsi = UPSI.objects.filter(Id = id).first()
    print(upsi.Attachment2)
    file = str(upsi.Attachment2)
    media_path = settings.MEDIA_ROOT
    file_path = os.path.join(media_path, file)
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        return HttpResponse(request, 'SSD_APP/edit_upsi.html')
    else:
        return HttpResponse(request, 'SSD_APP/edit_upsi.html')

class ViewAttachedPDF(View):
	def get(self, request, path):
            media_path = settings.MEDIA_ROOT
            file_path = os.path.join(media_path, path)
            print(file_path)
            return FileResponse(open(file_path, 'rb'), content_type='application/')


###############################################################################################


def reports_options(request):
    return render(request, 'SSD_APP/reports.html')

def generate_compilace_certificate(request):
    return render(request, 'SSD_APP/compilance_certificate.html')

def download_compilace_certificate_pdf(request):
    return render(request, 'SSD_APP/compilance_certificate.html')

def certificate_inputs(request):
    return render(request, 'SSD_APP/certificate_inputs.html')


###############################################################################################

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
            if request.method == "GET":
                first_name = request.GET.get('first_name')
                last_name = request.GET.get('last_name')
                designation = request.GET.get('designation')
                organization_name = request.GET.get('organization_name')
                number_of_event = request.GET.get('number_of_event')
                date_of_certification = request.GET.get('date_of_certification')
                place = request.GET.get('place')

                certificate_inputs = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'designation': designation,
                    'organization_name': organization_name,
                    'number_of_event': number_of_event,
                    'date_of_certification': date_of_certification,
                    'place': place,
                    }
                pdf = render_to_pdf('SSD_APP/compilance_certificate.html', certificate_inputs)
                return HttpResponse(pdf, content_type='application/pdf')
            raise BadRequest('Invalid request.')
