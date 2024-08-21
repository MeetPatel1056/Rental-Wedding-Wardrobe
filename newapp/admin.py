from django.contrib import admin

from newapp .models import *

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 10),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['User_id', 'Product_id', 'Price','From_Date','To_Date']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.User_id, obj.Product_id, obj.Price,obj.From_Date,obj.To_Date])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

def export_to_pdf2(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['Name', 'Email_id', 'Phone_no','Address','Status']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.Name, obj.Email_id, obj.Phone_no,obj.Address,obj.Status])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"



# Register your models here.
class Show_User(admin.ModelAdmin):
    list_display = ["Name","Email_id","Phone_no","Password","Status","Address"]
    actions = [export_to_pdf2]
admin.site.register(User,Show_User)

class Show_Category(admin.ModelAdmin):
    list_display = ["Category_Name"]
admin.site.register(Category,Show_Category)

class Show_Sub_cat(admin.ModelAdmin):
    list_display = ["Sub_catName","Category_id"]
admin.site.register(Sub_cat,Show_Sub_cat)

class Show_Product(admin.ModelAdmin):
    list_display = ["admin_photo","Category_id","Sub_Category_id","Product_name","Rent","Product_color","Product_size","Product_description","image","Status"]
admin.site.register(Product,Show_Product)


class Show_Order(admin.ModelAdmin):
    list_display = ["User_id","Product_id","Size","Address","Price","Status","From_Date","To_Date","Time_stamp"]
    list_filter = ['Time_stamp']
    actions = [export_to_pdf]


admin.site.register(order,Show_Order)


class Show_Card(admin.ModelAdmin):
    list_display = ["Name","Card_number","Cvv","Expiry_date","Time_stamp"]
admin.site.register(Card,Show_Card)

class Show_Payment(admin.ModelAdmin):
    list_display = ["User_id","Order_id","Payment_Method","Amount","Trans_id","Timestamp","Status"]
admin.site.register(Payment,Show_Payment)

class Show_Feedback(admin.ModelAdmin):
    list_display = ["User_id","Product_id","Rating","Comment","Timestamp"]
admin.site.register(Feedback,Show_Feedback)

class Show_Inquiry(admin.ModelAdmin):
    list_display = ["Name","Email","Phone","Timestamp","Message"]
admin.site.register(Inquiry,Show_Inquiry)


class Show_wishlist(admin.ModelAdmin):
    list_display = ["User_id", "Product_id"]
admin.site.register(Wishlist,Show_wishlist)