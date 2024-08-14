from django.urls import path
from .views import loginView , logoutView , incidentList ,mesIncident , createIncident , editIncident , showIncident
from .views import superadmin_dashbord , signup_view , user_delete ,user_edit , user_list
from .views import platform_create , platform_delete , platform_edit , platform_list 
from .views import envoi_mail , add_event , cellule_view , delete_event
from .views import stat_per_platforms , stat_per_year
from .views import list_couches , create_couche , edit_couche , delete_couche
from . import views
from .views import platform_chart

urlpatterns = [
    path("", loginView, name="login"),
    path("logout/", logoutView, name="logoutView"),

    path("adminapp/", incidentList, name="adminapp"),
    path("mesincident/",mesIncident , name="mesIncident"),
    path("createIncident/", createIncident, name="createIncident"),
    path("adminapp/<str:incident_id>", showIncident, name="showIncident"),
    path("adminapp/edit/<str:incident_id>",editIncident, name="editIncident"),

    path("superadmin/",superadmin_dashbord, name="superadmin"),
    path("signup/",signup_view, name="signup"),
    path("superadmin/user/",user_list, name="user_list"),
    path("superadmin/user/delete/<str:username>", user_delete, name="user_delete"),
    path("superadmin/user/<str:username>", user_edit, name="user_edit"),

    path("superadmin/platform/create/", platform_create, name="platform_create"),
    path("superadmin/platform/", platform_list, name="platform_list"),
    path("superadmin/platform/edit/<int:platform_id>",platform_edit, name="platform_edit"),
    path("superadmin/platform/delete/<int:platform_id>",platform_delete, name="platform_delete"),

    path("envoi_mail/",envoi_mail, name="envoi_mail"),
    path("cellule_de_crise/", cellule_view, name="cellule_de_crise"),
    path("add_event/", add_event , name="add_event"),
    path("delete_event/", delete_event, name="delete_event"),

    path("statestiques/stat_per_platforms/",stat_per_platforms, name="stat_per_platforms"),
    path("statestiques/stat_per_year/<int:year>",stat_per_year, name="stat_per_year"),

    path("list_couches/", list_couches , name="list_couches"),
    path("create_couche/", create_couche , name="create_couche"),
    path("edit_couche/<int:couche_id>", edit_couche , name="edit_couche"),
    path("delete_couche/<int:couche_id>", delete_couche , name="delete_couche"),
    
    
    path('stats/', views.dashboard, name='stats'),  
    path('get_incidents_data', views.get_incidents_data, name='get_incidents_data'),  
    path('platform-chart/', platform_chart, name='platform_chart'),
]
