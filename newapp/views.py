import uuid

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def index(request):
    context=basic(request)
    return render(request, "index.html",context)

def contact(request):
    context = basic(request)
    return render(request,"contact.html",context)

def blog(request):
    return render(request,"blog.html")

def product(request, pid):
    context = basic(request)
    data=Product.objects.get(id=pid)
    context.update({'productdata':data})
    return render(request,"product-details.html",context)

def subcatpage(request,sid):
    context = basic(request)
    fetchqueary=Product.objects.filter(Sub_Category_id=sid,Status="Available")
    context.update({"fetchdata":fetchqueary})
    return render(request,"Subcat.html",context)

def Men(request):
    context = basic(request)
    fetchqueary=Product.objects.filter(Category_id=2,Status="Available")
    subcat = Sub_cat.objects.filter(Category_id=2)
    context.update({"fetchdata": fetchqueary,"subcatdata": subcat})
    return render(request,"Men.html",context)

def Women(request):
    context = basic(request)
    fetchqueary=Product.objects.filter(Category_id=3,Status="Available")
    subcat = Sub_cat.objects.filter(Category_id=3)
    context.update({"fetchdata": fetchqueary,"subcatdata": subcat})
    return render(request,"Women.html",context)

def checkout(request):
    return render(request,"checkout.html")

def basic(request):
    try:
        lid=request.session['user_id']

        fetchqueary = Product.objects.all()
        data=order.objects.filter(User_id=lid).count()
        datatwo=Wishlist.objects.filter(User_id=lid).count()
        context={"fetchdata":fetchqueary,
                 "data":data,
                 "datatwo":datatwo}

        return context
    except:
        fetchqueary = Product.objects.all()
        context={"fetchdata":fetchqueary}
        return context

def signup(request):
    context = basic(request)
    return render(request,"Signup.html",context)

def login(request):
    context = basic(request)
    return render(request,"Login.html",context)

def insertdata(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        useremail = request.POST.get("uemail")
        userphone = request.POST.get("uphone")
        userpwd = request.POST.get("upassword")
        useraddress = request.POST.get("uaddress")
        queary = User.objects.filter(Email_id=useremail)
        if queary.exists():
            messages.error(request,'Email already exists!!')
            return render(request,"Signup.html")
        else:
            queary=User(Name=username,Email_id=useremail,Phone_no=userphone,Password=userpwd,Address=useraddress,Status="Active")
            queary.save()
            messages.success(request,'REGISTRATION SUCCESSFUL!!')
            return render(request, "Login.html")
    else:
        messages.error(request, 'SORRY!! UNABLE TO INSERT!!')
        return render(request,"Signup.html")

def CheckLogin(request):
     useremail=request.POST['uemail']
     userpwd=request.POST['upassword']
     try:
         query=User.objects.get(Email_id=useremail,Password=userpwd)
         request.session['useremail']=query.Email_id
         request.session['user_id'] = query.id
         request.session.save()
         print(request.session['user_id'])
     except User.DoesNotExist:
         query=None
     if query is not None:
         messages.success(request, 'LOGIN SUCCESSFUL!!')
         return redirect(index)
     else:
         messages.info(request,'Account Does Not Exists !! Please Sign Up')
     return render(request,"Signup.html")

def logout(request):
    try:
        del request.session['useremail']
        del request.session['user_id']
    except:
        pass
    return redirect(index)


def editprofile(request):
    Login_Id = request.session['user_id']
    query=User.objects.get(id=Login_Id)
    return render(request,"editprofile.html",{"userdata":query})

def updateprofile(request):
    Name=request.POST.get("uname")
    Email=request.POST.get("uemail")
    Phone=request.POST.get("uphone")
    Password = request.POST.get("upassword")
    Address = request.POST.get("uaddress")
    Login_Id = request.session['user_id']
    query= User.objects.get(id=Login_Id)
    query.Name = Name
    query.Email_id = Email
    query.Phone_no = Phone
    query.Password = Password
    query.Address = Address
    query.save()
    return redirect(index)

def Insert_Contact(request):
    name = request.POST.get("Name")
    email = request.POST.get("Email")
    phone = request.POST.get("Phone")
    message = request.POST.get("Message")
    queary = Inquiry(Name=name,Email=email,Phone=phone,Message=message)
    queary.save()
    messages.success(request,'DETAILS ARE SUCCESSFULLY ADDED WE WILL CONTACT YOU SOON!!')
    return render(request,"contact.html")

def Place_Order(request):
    lid = request.session['user_id']
    Pro_id = request.POST.get("pid")
    Rent = request.POST.get("totalAmount")
    fromdate=request.POST.get("fromDate")
    todate=request.POST.get("toDate")
    address=request.POST.get("address")
    if request.method=="POST":
       pay_method = request.POST.get("paymentMode")
       print(pay_method)
       if pay_method=="offline":
          insertorder = order(User_id=User(id=lid),Address=address,To_Date=todate,From_Date=fromdate,Product_id=Product(id=Pro_id),Price=Rent,Status="Confirm")
          insertorder.save()
          order_id = insertorder.id
          insertpayment=Payment(User_id=User(id=lid),Order_id=order(id=order_id),Payment_Method=pay_method,
                            Status="Paid",Amount=Rent,Trans_id = 0)
          insertpayment.save()

          updatestatusofproduct = Product.objects.get(id=Pro_id)
          updatestatusofproduct.Status = "Not Available"
          updatestatusofproduct.save()


          messages.success(request,'order placed successfully')
       elif pay_method=="online":
            cname= request.POST.get("cardName")
            cnumber= request.POST.get("cardNumber")
            Cvv= request.POST.get("cvv")
            expiry_date= request.POST.get("expiryDate")
            carddata= Card.objects.first()
            name=carddata.Name
            number=carddata.Card_number
            cvv=carddata.Cvv
            expiry=carddata.Expiry_date
            balance=carddata.Card_Balance
            if cname==name and number==int(cnumber) and cvv==int(Cvv) and expiry_date==expiry and int(Rent)<balance:
                insertorder = order(User_id=User(id=lid),Address=address,To_Date=todate, From_Date=fromdate,
                                    Product_id=Product(id=Pro_id), Price=Rent, Status="Confirm")
                insertorder.save()
                order_id = insertorder.id
                transaction_id = str(uuid.uuid4())
                insertpayment = Payment(User_id=User(id=lid), Order_id=order(id=order_id), Payment_Method=pay_method,
                                        Status="Paid", Amount=Rent, Trans_id=transaction_id)
                insertpayment.save()
                updatestatusofproduct = Product.objects.get(id=Pro_id)
                updatestatusofproduct.Status = "Not Available"
                updatestatusofproduct.save()

                messages.success(request, 'order placed successfully')
            else:
                messages.error(request,"Transaction Failed")
    return redirect(booking_history)



def booking_history(request):
    context = basic(request)
    lid=request.session['user_id']
    fetchquery=order.objects.filter(User_id=lid)
    orders_with_ddate = []

    # Loop through each order instance in fetchquery

    context.update({"fetchdata": fetchquery,
                    "fdate":orders_with_ddate,
                    })
    return render(request,"booking_history.html",context)

def wishlist(request):
    context = basic(request)
    lid = request.session['user_id']
    fetchdata = Wishlist.objects.filter(User_id=lid)
    context.update({
        "dataone":fetchdata
    })
    return render(request,"wishlist.html",context)

def Insert_wishlist(request,id):
    lid=request.session['user_id']
    try:
        fetch=Wishlist.objects.get(User_id=lid,Product_id=id)
        messages.info(request,'product already exist in wishlist')
    except:
        queary=Wishlist(User_id=User(id=lid),Product_id=Product(id=id))
        queary.save()
    return redirect(wishlist)

def cancelbooking(request,id):
    fetchdetails = order.objects.get(id=id)
    fetchdetails.Status = "Cancelled"
    fetchdetails.save()
    return redirect("/booking_history")

def feedback(request,fid):
    context = basic(request)
    context.update({"fid":fid})
    return render(request,"feedback.html",context)

def Insert_Feedback(request):
    try:
        lid = request.session['user_id']
        Pro_id = request.POST.get("pid")
        rating = request.POST.get("rating")
        comment = request.POST.get("Message")
        queary = Feedback(User_id=User(id=lid),Product_id=Product(id=Pro_id),Rating=rating,Comment=comment)
        queary.save()
        messages.success(request, 'Thank You For Giving Feedback US')
    except:
        messages.error(request, 'Error occured!')

    return render(request,'index.html')


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['email']
        try:
            user = User.objects.get(Email_id=username)

        except User.DoesNotExist:
            user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = User.objects.get(Email_id=username)
            cuser.Password = password
            cuser.save(update_fields=['Password'])

            print('Mail sent')
            messages.info(request, 'Mail Is Sent')
            return redirect(index)

        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)

def forgot(request):
    return render(request,"forgot_password.html")

