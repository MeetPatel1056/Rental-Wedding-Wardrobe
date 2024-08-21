from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('contact', views.contact, name="contact us"),
    path('feedback/<int:fid>',views.feedback,name="feedback"),
    path('blog', views.blog, name="Blog"),
    path('product-details/<int:pid>', views.product, name="product-details"),
    path('checkout', views.checkout, name="checkout"),
    path('basic', views.basic, name="basic"),
    path('login', views.login, name="login"),
    path('CheckLogin', views.CheckLogin, name="CheckLogin"),
    path('logout',views.logout,name="logout"),
    path('signup', views.signup, name="signup"),
    path('insert', views.insertdata, name="insert"),
    path('subcatpage/<int:sid>', views.subcatpage, name="subcatpage"),
    path('Men', views.Men, name="Men"),
    path('Women', views.Women, name="Women"),
    path('editprofile', views.editprofile, name="edit"),
    path('updateprofile',views.updateprofile,name="update"),
    path('insert_contact',views.Insert_Contact,name="Insert_Contact"),
    path('placeorder',views.Place_Order,name="Place_Order"),
    path('booking_history',views.booking_history,name="booking_history"),
    path('Wishlist',views.wishlist,name="Wishlist"),
    path('Insert_wishlist/<int:id>',views.Insert_wishlist,name="Insert_wishlist"),
    path('cancelbooking/<int:id>',views.cancelbooking,name="cancelbooking"),
    path('insert_feedback', views.Insert_Feedback, name="Insert_Feedback"),
    path('forgot',views.forgot,name="feedback"),
    path('forgot_password',views.forgotpassword,name="forgotpassword")
]


