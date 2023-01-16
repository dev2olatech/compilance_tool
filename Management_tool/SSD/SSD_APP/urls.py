from django.urls import path, include
from SSD_APP import views
from django.conf import settings
from django.conf.urls.static import static

# Create a end point for view function

urlpatterns = [
    path('',views.home, name = "home"),

# path for the login, logout, register
    path("register/", views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


# path for the users function 
    path('manage_users', views.Users_View, name = 'manage_users'),
    path('add_user', views.user_addition, name = 'add_user'),
    path('edit/<str:id>', views.user_edit, name='edit'),
    path('update/<str:id>', views.user_update, name='update'),

 # path for the make disclosure function 
    path('make_disclosure', views.Make_Disclosure, name = 'make_disclosure'),
    path('add_reports', views.disclosure_addition, name = 'add_reports'),
    path('dedit/<str:id>', views.disclosure_edit, name='dedit'),
    path('dupdate/<str:id>', views.disclosure_update, name='dupdate'),
    path('DeleteDisclosureAttachedPDF', views.DeleteDisclosureAttachedPDF, name="DeleteDisclosureAttachedPDF"),


# path for the upsi function
    path('manage_upsi', views.UPSI_View, name = 'manage_upsi'),
    path('add_upsi', views.upsi_addition, name = 'add_upsi'),
    # path('add_upsi_attchment', views.upsi_attachment_addition, name = 'add_upsi_attchment'),


# path for the report function
    path('reports', views.reports_options, name = 'reports'),
    path('certificate_inputs', views.certificate_inputs, name = 'certificate_inputs'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),  # path for the view and download certificate


# path for the UPSI Modules
    path('manage_upsi', views.UPSI_View, name = 'manage_upsi'),
    path('add_upsi', views.upsi_addition, name = 'add_upsi'),
    path('edit_upsi/<str:id>', views.upsi_edit, name = 'edit_upsi'),
    path('uupdate/<str:id>', views.upsi_update, name='uupdate'),
    path('show_attched_pdf/<str:path>', views.ViewAttachedPDF.as_view(), name="show_attched_pdf"),
    path('delete_attched_pdf1', views.DeleteAttachedPDF1, name="delete_attched_pdf1"),
    path('delete_attched_pdf2', views.DeleteAttachedPDF2, name="delete_attched_pdf2"),

    # path('delete_attched_pdf/<str:id>', views.DeleteAttachedPDF, name="delete_attched_pdf"),



] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)

