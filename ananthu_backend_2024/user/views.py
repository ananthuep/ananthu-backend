from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from.models import docters,staff,patients,BOOKING,Registration
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import make_password ,check_password
from django.contrib.auth import logout
from django.http import JsonResponse,HttpResponse
from .serializer import registerserializer
# Create your views here.
@csrf_exempt
def hashregister (request):
    if request.method=='POST':
        name=request.POST.get('fname')
        age=request.POST.get('fage')
        contact=request.POST.get('fcontact')
        password=request.POST.get('fpassword')
        username=request.POST.get('fusername')
        category=request.POST.get('fcatagory')
        dob = request.POST.get('fdob')

        if Registration.objects.filter(USERNAME=username).exists():
            return JsonResponse({"error":"username already exists"})
        else:
            if category=='docter':
                docters.objects.create(NAME=name,AGE=age,CONTACT=contact,USERNAME=username,CATEGORY=category, DATE_OF_BIRTH=dob)
                Registration.objects.create(NAME=name,USERNAME=username,AGE=age,CATEGORY=category,PASSWORD=make_password(password),CONTACT=contact) 
                return JsonResponse({'status':'REGISTRATION SUCCESS'})
            elif category== 'staff':
                staff.objects.create(NAME=name,USERNAME=username,AGE=age,CATEGORY=category,CONTACT=contact,DATE_OF_BIRTH=dob)
                Registration.objects.create(NAME=name,USERNAME=username,AGE=age,CATEGORY=category,PASSWORD=make_password(password),CONTACT=contact)
                return JsonResponse({'status':'REGISTRATION SUCCESS'})
            else:
               patients.objects.create(NAME=name,USERNAME=username,AGE=age,CATEGORY=category,CONTACT=contact,DATE_OF_BIRTH=dob)
               Registration.objects.create(NAME=name,USERNAME=username,AGE=age,CATEGORY=category,PASSWORD=make_password(password),CONTACT=contact)

               return JsonResponse({'status':'REGISTRATION SUCCESS'})
    
    else:
         return JsonResponse({"error":"method is wrong"})
    
@csrf_exempt
def login(request):
   if request.session.get('user_id'):
       return JsonResponse({'success':"your already login"})
   
   if request.method == 'POST':
      user_name =request.POST.get('fusername')
      password = request.POST.get('fpassword')

      if Registration.objects.filter(USERNAME=user_name).exists():
          
          data=Registration.objects.get(USERNAME=user_name)

          if data.USERNAME==user_name and check_password(password,data.PASSWORD):           
              Response=JsonResponse({'success':'login'})
              Response.set_cookie('logincookie','cookivalue',max_age=3600)

              request.session['username']=data.USERNAME
              request.session['user_id']=data.id

              return Response
          else:
              return JsonResponse({'error':'password is wrong'})
      else:
          return JsonResponse({'error':'no user found'})

# update details
@csrf_exempt
def logouts(request):
    logout(request)
    responce=JsonResponse({'success':'logout'})
    responce.delete_cookie('logincookie')
    return responce
@csrf_exempt   
def doctor(request):
    name=request.POST.get('name')
    AGE=request.POST.get('AGE')
    CONTACT=request.POST.get('contact')
    DATE_OF_BIRTH=request.POST.get('date_of_birth')
    USERNAME=request.POST.get('username')

    if docters.objects.filter(USERNAME=USERNAME).exists():
        data=docters.objects.get(USERNAME=USERNAME)
        data.NAME=name
        data.AGE=AGE
        data.CONTACT=CONTACT
        data.DATE_OF_BIRTH=DATE_OF_BIRTH

        data.save()

        return JsonResponse({'success':"data entry successfully"})
    else:
         return JsonResponse({'error':"USERNAME is wrong"})
@csrf_exempt
def staffs(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    CONTACT=request.POST.get('contact')
    date_of_birth=request.POST.get('date_of_birth')
    username=request.POST.get('username')
    
    if staff.objects.filter(USERNAME=username).exists():
        data=staff.objects.get(USERNAME=username)
        data.NAME=name
        data.AGE= age
        data.CONTACT=CONTACT
        data.DATE_OF_BIRTH=date_of_birth
        data.USERNAME=username

        data.save()
        return JsonResponse({'success':"data entry successfully"})
    else:
        return JsonResponse({'error':"AGE is wrong"})
@csrf_exempt
def  patient(request):
    name=request.POST.get('name')
    AGE= request.POST.get('age')
    CONTACT=request.POST.get('contact')
    date_of_birth=request.POST.get('date_of_birth')
    username=request.POST.get('username')    

    if patients.objects.filter(NAME=name).exists():
       data=patients.objects.get(NAME=name)
       data.AGE=AGE
       data.CONTACT=CONTACT
       data.DATE_OF_BIRTH=date_of_birth
       data.USERNAME=username
        
       data.save()
       return JsonResponse({'success':"data entry successfully"})
    
    else: 

      return JsonResponse({'error':"NAME IS WRONG"})
@csrf_exempt   
def  BOOKINGS (request):
     name= request.POST.get('name')
     age=request.POST.get('age')
     gender=request.POST.get('gender')
     date_of_birth=request.POST.get('date_of_birth')
     Contact=request.POST.get('phone')

     if BOOKING.objects.filter(CONTACT=Contact).exists():
        
         return JsonResponse({'error':"booking already"})
     else: 
         BOOKING.objects.create(CONTACT=Contact,NAME=name,AGE=age,DATE_OF_BIRTH=date_of_birth,GENDER=gender)
         return JsonResponse({'success':'booked successfully'})
         
     

@csrf_exempt
def deletedetails(request):
    if request.method=='POST':
        username=request.POST.get('username')
        if Registration.objects.filter(USERNAME=username).exists():
           data =Registration.objects.get(USERNAME=username)
           category=data.CATEGORY
           if category=='docter':
               docters.objects.get(USERNAME=username).delete()
               Registration.objects.get(USERNAME=username).delete()
               return JsonResponse({'status':'deleted '})
           if category=='staff':
               staff.objects.get(USERNAME=username). delete()
               Registration.objects.get(USERNAME=username).delete()
               return JsonResponse({'status':'deleted '})
           if category=='patient':
               patients.objects.get(USERNAME=username).delete()
               Registration.objects.get(USERNAME=username).delete()
               return JsonResponse({'status':'deleted '})
            
        else: 
            return JsonResponse({'error':'user name not found'})
    else: 
        return JsonResponse({'error':'method is worng'})      
    

@csrf_exempt
def displaydata(request):
    if  request.method =='POST':
        username= request.POST.get('username')
        if  Registration.objects.filter(USERNAME=username).exists():
            user=Registration.objects.get(USERNAME=username)
            serializer=registerserializer(user)
            return JsonResponse({'status':'success','data':serializer.data})
        else:
            return JsonResponse({'error':'USER NOT FOUND'})
    else: return JsonResponse({'error':'NO DATA'})

def   serchdetails(request,name):
    if name:
       data=Registration.objects.filter(NAME__icontains=name) | Registration.objects.filter(USERNAME__icontains=name)|Registration.objects.filter(CONTACT__icontains=name)|Registration.objects.filter(AGE__icontains=name)
       serializer= registerserializer(data,many=True)
       return JsonResponse({'status':'SUCCESS','data':serializer.data}) 
    else:
        return JsonResponse({'error':'USER NOT FOUND'})


