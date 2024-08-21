from django.db import models
from django.utils.safestring import mark_safe

USERSTATUS={
    ("Inactive","Inactive"),
    ("Active","Active"),
}

PRODUCTSTATUS={
    ("Not Available","Not Available"),
    ("Available","Available")
}

ORDERSTATUS={
    ("Pending","Pending"),
    ("Confirm","Confirm"),
    ("Cancelled","Cancelled"),
}

PAYMENTSTATUS={
    ("Paid","Paid"),
    ("Unpaid","Unpaid")
}

COMPLAINSTATUS={
    ("Solved","Solved"),
    ("Unsolved","Unsolved")
}

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=25)
    Email_id=models.EmailField()
    Phone_no=models.BigIntegerField()
    Password=models.CharField(max_length=25)
    Status=models.CharField(max_length=25,choices=USERSTATUS)
    Address=models.CharField(max_length=100)


    def __str__(self):
        return self.Name

class Category(models.Model):
    Category_Name=models.CharField(max_length=25)

    def __str__(self):
        return self.Category_Name

class Sub_cat(models.Model):
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    Sub_catName=models.CharField(max_length=70)

    def __str__(self):
        return self.Sub_catName

class Product(models.Model):
    Category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    Sub_Category_id = models.ForeignKey(Sub_cat, on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Rent=models.CharField(max_length=20)
    Product_color=models.CharField(max_length=20)
    Product_size=models.CharField(max_length=20)
    Product_description=models.TextField()
    image=models.ImageField(upload_to='photos')
    Status=models.CharField(max_length=25,choices=PRODUCTSTATUS)

    def __str__(self):
        return self.Product_name

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))


class order(models.Model):
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Price=models.FloatField()
    Size=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    From_Date=models.DateField(null=True)
    To_Date=models.DateField(null=True)
    Status=models.CharField(max_length=25,choices=ORDERSTATUS)
    Time_stamp = models.DateTimeField(auto_now=True, editable=False)

class Card(models.Model):
    Name=models.CharField(max_length=25)
    Card_number=models.IntegerField()
    Cvv=models.IntegerField()
    Expiry_date=models.CharField(max_length=30)
    Card_Balance=models.FloatField(default=100000)
    Time_stamp=models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.Name

class Payment(models.Model):
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Order_id=models.ForeignKey(order,on_delete=models.CASCADE)
    Payment_Method=models.CharField(max_length=20,choices=[("online","online"),("offline","offline")])
    Amount=models.FloatField()
    Trans_id=models.CharField(max_length=23,null=True)
    Timestamp=models.DateTimeField(auto_now=True,editable=False)
    Status=models.CharField(max_length=20,choices=PAYMENTSTATUS)

class Feedback(models.Model):
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Rating=models.IntegerField()
    Comment=models.TextField()
    Timestamp=models.DateTimeField(auto_now=True,editable=False)

class Inquiry(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.BigIntegerField()
    Timestamp=models.DateTimeField(auto_now=True,editable=False)
    Message=models.TextField()

    def __str__(self):
        return self.Name


class Wishlist(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

