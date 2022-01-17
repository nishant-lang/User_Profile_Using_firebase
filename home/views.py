from distutils.command import config
from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {   
  "apiKey": "AIzaSyCl6SY_bE3ZR2Wd-ycBwlnJXZTtWqRnTxw",
  "authDomain": "krishweb-23068.firebaseapp.com",
  "databaseURL": "https://krishweb-23068-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "krishweb-23068",
  "storageBucket": "krishweb-23068.appspot.com",
  "messagingSenderId": "77154858909",
  "appId": "1:77154858909:web:6bcd2bd63dd16bd69d2174",
  "measurementId": "G-1Z4985Z6PN"
}
firebase = pyrebase.initialize_app(config)
database= firebase.database()
authe = firebase.auth()
storage = firebase.storage()

posts=[
    {
    'author':'NIshant',
    'title':'Blog post 1',
    'content':'Friest post content ',
    'date_posted':'Jan 15,2022 '
},
    {
    'author':'Ram',
    'title':'Blog post 2',
    'content':'Second post content ',
    'date_posted':'Jan 16,2022 '
},

]

def index(request):
   
    context={
        'posts':posts
    }
    return render(request,"index.html",context)
   
# def new(request):
    # name=database.child('data').child('name').get.val()
    # age=database.child('data').child('age').get.val()
    # posts=database.child('data').child('post').get.val()
    # email=database.child('data').child('email').get.val()
    # return render(request,"new.html",{"name":name},{"age":age},{"posts":posts},{"email":email})

def login(request):
    
    return render(request,"login.html")

def logedin(request):

    email=request.POST.get("email")
    password=request.POST.get("password")
    try:
       user = authe.sign_in_with_email_and_password(email,password) 
    except: 
        message="Invalid Credentials"
        return render (request,"login.html",{"message":message})


    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render (request,"logedin.html",{"email":email})

def signup (request):
   return render(request,"signup.html")

def signedup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')

    try:  
       user=authe.create_user_with_email_and_password(email,password)
    
    except: 
        message="User allReady Exits"
        return render(request,"signup.html",{"message":message})

    uid=user['localId']

    data={"name":name,'status':'1'}

    database.child("users").child(uid).child("details").set(data)
    message="User added Sucessfully"
    return render(request,"login.html",{"message":message})
    

def logout(request):
    
    auth.logout(request)
    return render(request,"login.html")
   
def about(request):
    return render(request,"about.html",{'title':'About'})


def reset(request):
    return render(request,"reset.html")
    
def postReset(request):  
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"
        return render(request, "Reset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg":message})
    

