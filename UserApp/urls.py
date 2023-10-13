from django.urls import path
from.import views

urlpatterns = [
    path('',views.UserIndex,name='UserIndex'),
    path('About',views.About,name='About'),
    path('BookVenues/<int:id>/',views.BookVenues,name='BookVenues'),
    path('Bookdata/<int:id>',views.Bookdata,name='Bookdata'),
    path('ContactUs',views.ContactUs,name='ContactUs'),
    path('Locations',views.Locations,name='Locations'),
    path('Login',views.Login,name='Login'), 
    path('Register',views.Register,name='Register'),
    path('Venues',views.Venues,name='Venues'),
    path('ContactData',views.ContactData,name='ContactData'),
    path('RegisterData',views.RegisterData,name='RegisterData'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('OnecardVenue/<int:id>',views.OnecardVenue,name='OnecardVenue'),
    path('OneLocation/<str:street>',views.OneLocation,name='OneLocation')
]    