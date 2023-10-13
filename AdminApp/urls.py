from django.urls import path
from.import views

urlpatterns = [
path('AdminIndex',views.AdminIndex,name='AdminIndex'),
path('AddLocation',views.AddLocation,name='AddLocation'),
path('AddManager',views.AddManager,name='AddManager'),
path('AddVenue',views.AddVenue,name='AddVenue'),
path('Bookings',views.Bookings,name='Bookings'),
path('Feedbacks',views.Feedbacks,name='Feedbacks'),
path('RegisteredUsers',views.RegisteredUsers,name='RegisteredUsers'),
path('ViewManageLocations',views.ViewManageLocations,name='ViewManageLocations'),
path('ViewManageManager',views.ViewManageManager,name='ViewManageManager'),
path('ViewManageVenues',views.ViewManageVenues,name='ViewManageVenues'),
path('LocationData',views.LocationData,name='LocationData'),
path('EditLocation',views.EditLocation,name='EditLocation'),
path('EditLoc/<int:id>',views.EditLoc,name='EditLoc'),
path('UpdateLocation/<int:id>',views.UpdateLocation,name='UpdateLocation'),
path('DeleteLocation/<int:id>',views.DeleteLocation,name='DeleteLocation'),
path('VenueData',views.VenueData,name='VenueData'),
path('EditVenue',views.EditVenue,name='EditVenue'),
path('EditVen/<int:id>',views.EditVen,name='EditVen'),
path('UpdateVenue/<int:id>',views.UpdateVenue,name='UpdateVenue'),
path('DeleteVenue/<int:id>',views.DeleteVenue,name='DeleteVenue'),
path('Managerdata',views.Managerdata,name='Managerdata'),
path('EditManger',views.EditManger,name='EditManger'),
path('EditMan/<int:id>',views.EditMan,name='EditMan'),
path('UpdateManager/<int:id>',views.UpdateManager,name='UpdateManager'),
path('DeleteManager/<int:id>',views.DeleteManager,name='DeleteManager')
]
