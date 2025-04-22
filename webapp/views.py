from django.shortcuts import render, redirect
from .models import *
from .BlockChain import load_contract_address, add_data, dataget
from .IPFS import ipfsget
from django.http import FileResponse
# Create your views here.


def home(request):
    load_contract_address()
    return render(request, 'index.html')

def loginaction(request):
    pwd = request.POST['pwd']
    uid = request.POST['uid']
    role = request.POST['role']

    if role == 'admin':
        if uid == 'COE' and pwd == 'COE':
            return render(request, 'admin_home.html')
        else:
            stz = True
            return render(request, 'index.html', {'msg': "COE Login details are invalid !! ", 'stz': stz})
    elif role == 'superintendent':
        d = superintendent.objects.filter(email=uid).filter(password=pwd)
        d1 = d.count()
        if d1 > 0:
            request.session['semail'] = uid

            request.session['sname'] = d[0].name
            return render(request, 's_home.html')

        else:
            stz = True
            return render(request, 'index.html', {'msg': "Superintendent Login details are invalid !! ", 'stz': stz})
    elif role == 'teacher':
        d = teachers.objects.filter(email=uid).filter(password=pwd)
        d1 = d.count()
        if d1 > 0:
            request.session['temail'] = uid
            request.session['tname'] = d[0].name

            
            return render(request, 't_home.html')
    elif role == 'recipient':
        d = recipient.objects.filter(email=uid).filter(password=pwd)
        d1 = d.count()
        if d1 > 0:
            request.session['remail'] = uid
            request.session['rname'] = d[0].name

            
            return render(request, 'r_home.html')

        else:
            stz = True
            return render(request, 'index.html', {'msg': "Recipient Login details are invalid !! ", 'stz': stz})

    else:
        stz = True
        return render(request, 'index.html', {'msg': "Login details are invalid !! ", 'stz': stz})



def adminhome(request):
    if True:
        return render(request, 'admin_home.html',)

    else:
    	pass
def adminlogout(request):
    return render(request, 'index.html')		

		
		
	

	
def addstaff(request):
    return render(request, 'addstaff.html', )		
		
	
def viewstaff(request):
    
    d=superintendent.objects.all()
    return render(request, 'viewstaff.html', {'data':d,})		
	


def addstaffaction(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    designation = request.POST['designation']
    

    password = request.POST['password']
    
    d = superintendent(name=name, email=email, phone=phone,  designation=designation, password=password)
    d.save()

    

    return render(request, 'addstaff.html', { 'msg': "Superintendent Account Created !! "})

	

def teachersignup(request):
    
    return render(request, 'teachersignup.html',)




def teachersignupaction(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    password=request.POST['password']

    work_exp = request.POST['work_exp']
    work_address = request.POST['work_address']
    subject = request.POST['subject']
    
    d = teachers(name=name,   email=email, phone=phone,
              address=address, work_address=work_address, work_exp=work_exp, password=password, subject=subject)
    d.save()
 
    return render(request, 'teachersignup.html', { 'msg':'Signup completed !!'})		
		


def shome(request):
    if "semail" in request.session:
        return render(request, 's_home.html',)
    else:
        stz=True
        return render(request, 'index.html', {'msg':"Your session is expired !! ", 'stz':stz})


def viewteachers(request):
    d=teachers.objects.all()
    return render(request, 'viewteachers.html', {'data':d})


def slogout(request):
    try:
        del request.session['semail']
    except:
        pass
    return render(request, 'index.html')		


def paper_request_def(request):
    if request.method=="POST":
        sub=request.POST['sub']
        ename=request.POST['ename']
        eid=request.POST['eid']
        
        d=paper_request(examid=eid, exam_name=ename, subject=sub, stz="Request Sent")
        d.save()
        return render(request, "paper_request.html", {'msg':'Request Sent to Superintendent !!'})
    else:
        return render(request, "paper_request.html")

def viewpaperrequest(request):
    if request.method=="POST":
        data=request.POST['data']
        name=data.split(';')[0]
        email=data.split(';')[1]
        id=request.POST['id']
        check=alloted_teachers.objects.filter(eid=id).filter(teacher_email=email).count()

        if check>0:
            p=paper_request.objects.filter(stz="Request Sent")
            t=teachers.objects.all()
            return render(request, "viewpaperrequest.html", {'p':p, 't':t, 'msg':'ERROR:: This teacher is already allocated for this job !!'})
        else:
            data=paper_request.objects.filter(id=id)[0]
            d=alloted_teachers(eid=id, exam_name=data.exam_name,\
            subject=data.subject, teacher_email=email, teacher_name=name, stz='new', pdf='non')
            
            d.save()
            p=paper_request.objects.filter(stz="Request Sent")
            t=teachers.objects.all()
            return render(request, "viewpaperrequest.html", {'p':p, 't':t, 'msg':'The teacher is allocated for this job !!'})



        

def paperrequestcomplete(request):
    if request.method=="POST":
        
        """data=request.POST['data']
        name=data.split(';')[0]
        email=data.split(';')[1]
        """
        
        id=request.POST['id']
        
        d=paper_request.objects.filter(id=id).update(stz="Alloted")
              
        
        p=paper_request.objects.filter(stz="Request Sent")
        t=teachers.objects.filter()
           
        return render(request, "viewpaperrequest.html", {'p':p, 't':t, 'msg':'Teachers are alloted to this job !!'})

    
    else:

        p=paper_request.objects.filter(stz="Request Sent")
        t=teachers.objects.filter()
        data=paper_request.objects.filter(stz="Alloted")
        
        
           
        return render(request, "viewpaperrequest.html", {'p':p, 't':t,'data':data})

def aviewpaperrequests(request):
    p=paper_request.objects.filter()
    return render(request, "aviewpaperrequests.html", {'p':p,})


def thome(request):
    if "temail" in request.session:
        return render(request, 't_home.html',)
    else:
        stz=True
        return render(request, 'index.html', {'msg':"Your session is expired !! ", 'stz':stz})

def teacher_paper_reqs(request):
    if 'temail' in request.session:
        email=request.session['temail']
        d=alloted_teachers.objects.filter(stz="new").filter(teacher_email=email)
        return render(request, 'teacher_paper_reqs.html', {'data':d})
    else:
        stz=True
        return render(request, 'index.html', {'msg':"Your session is expired !! ", 'stz':stz})

def tlogout(request):
    try:
        del request.session['temail']
    except:
        pass
    return render(request, 'index.html')		


def uploadpaper(request):
    email=request.session['temail']
    id=request.POST['id']
    file=request.POST['file']

    # from .IPFS import store
    # pdf = 'uploads//' + str(file)
    # pdf_cid = store(pdf)
    # print(pdf_cid, '<<<<<<<<<<<<<<<<<<<<')
    # data = [id, pdf_cid]
    # try:
    #     load_contract_address()
    #     add_data(email, data)
    #     



    # except Exception as e:
    #     print(f"Error interacting with the contract: {str(e)}")
    #     return render(request, 't_home.html', {'msg': "Error interacting with contract."})
    
    alloted_teachers.objects.filter(eid=id).filter(teacher_email=email).update(stz="Paper Uploaded", pdf=file)
    print(id, email)
    return render(request, 't_home.html', {'msg': "Paper Uploaded Successfully !!"})


        
def viewresponses(request):
    id=request.GET['id']
    data=alloted_teachers.objects.filter(eid=id).filter(stz='Paper Uploaded')
    return render(request, "viewresponses.html", {'data':data,})


def viewpdf(request, op):
    d=alloted_teachers.objects.filter(id=op)[0]
    pdffile=d.pdf
    file='uploads/'+pdffile
    return FileResponse(open(file, 'rb'), content_type='application/pdf')

def finalizepaper(request):
    id=request.GET['id']
    eid=request.GET['eid']
    paper=request.GET['paper']
    paper_request.objects.filter(id=eid).update(stz='Paper Finalized', paper=paper)
    alloted_teachers.objects.filter(id=id).update(stz='Paper Finalized')
    return render(request, 's_home.html', {'msg':'Paper Finalized !!'})



def view_paper(request, paper):
    file='uploads/'+paper
    return FileResponse(open(file, 'rb'), content_type='application/pdf')


def uploadipfs(request):
    id=request.POST['id']
    file=request.POST['file']
    examid=request.POST['examid']
    exam_name=request.POST['exam_name']
    subject=request.POST['subject']





    from .IPFS import store
    pdf = 'uploads//' + str(file)
    pdf_cid = store(pdf)
    print(pdf_cid, '<<<<<<<<<<<<<<<<<<<<')
    data = [id, examid, exam_name, subject, pdf_cid]
    try:
        load_contract_address()
        add_data('COE', data)
        



    except Exception as e:
        print(f"Error interacting with the contract: {str(e)}")
        return render(request, 't_home.html', {'msg': "Error interacting with contract."})
    
    paper_request.objects.filter(id=id).update(stz="Paper in dAPP")
    
    return render(request, 'admin_home.html', {'msg': "Paper Uploaded IPFS server and Data stored in block chain !!"})



def downloadfromipfs(request):
    id = request.POST.get('id')  # Use .get() to avoid KeyError
    pdffile=''
    
    try:
        # Load smart contract data
        load_contract_address()
        all_data = dataget()
        print(f"All data retrieved from the contract: {all_data}")
    except Exception as e:
        print(f"Error retrieving data from contract: {e}")
        return render(request, 'admin_home.html', {'msg': 'Error retrieving data from contract'})

    # Loop through the fetched data
    for data_list in all_data:
        try:
            print(f"Data List: {data_list}")

            block_id = data_list[0]
            ipfs_hash = data_list[4]

            if id == block_id:
                try:
                    ipfsget(ipfs_hash)  # Fetch data from IPFS
                    pdffile = f"{ipfs_hash}.pdf"
                    file_url = f"//downloads//{pdffile}"
                    
                    

                except ValueError as e:
                    pass
                    
                    

        except Exception as e:
            print(f"Error processing entry: {e}")
            continue

    # If no matching ID was found, return an error response
    return render(request, 'viewpdf.html', {'file':pdffile})


def viewfile(request):
    
    pdffile=request.POST["file"]
    file='downloads/'+pdffile
    return FileResponse(open(file, 'rb'), content_type='application/pdf')






def rsignup(request):
    
    return render(request, 'rsignup.html',)




def rsignupaction(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    
    password=request.POST['password']

    organization = request.POST['organization']
    org_address = request.POST['org_address']
    
    
    d = recipient(name=name,   email=email, phone=phone,
               organization=organization, org_address=org_address, password=password)
    d.save()
 
    return render(request, 'teachersignup.html', { 'msg':'Signup completed !!'})		
		




def rhome(request):
    if "remail" in request.session:
        return render(request, 'r_home.html',)
    else:
        stz=True
        return render(request, 'index.html', {'msg':"Your session is expired !! ", 'stz':stz})

def rlogout(request):
    try:
        del request.session['remail']
    except:
        pass
    return render(request, 'index.html')	

def viewpapers(request):
    try:
        # Load smart contract data
        load_contract_address()
        all_data = dataget()
        print(f"All data retrieved from the contract: {all_data}")

        data=[] #data = [id, examid, exam_name, subject, pdf_cid]
        

        for data_list in all_data:
            d={'id':data_list[0],'examid':data_list[1],'exam_name':data_list[2],'subject':data_list[3], 'pdf_cid':data_list[4]}
            data.append(d)
        return render(request, 'viewpapers.html', {'data':data})

    except Exception as e:
        print(f"Error retrieving data from contract: {e}")
        return render(request, 'r_home.html', {'msg': 'Error retrieving data from contract'})




def downloadfromipfs2(request):
    cid = request.POST.get('id')  # Use .get() to avoid KeyError
    pdffile=''
    
    try:
        #ipfsget(cid)  # Fetch data from IPFS
        pdffile = f"{cid}.pdf"
        file_url = f"downloads/{pdffile}"
                    
                    

    except ValueError as e:
        pass
                    
                    
    # If no matching ID was found, return an error response
    return render(request, 'viewpdf2.html', {'file':pdffile})

