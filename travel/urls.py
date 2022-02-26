"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tour import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('all_user/',views.all_user,name='all_user'),
    path('add_destination/',views.add_destination,name='add_destination'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('destination/',views.destination,name='destination'),
    path('discount/',views.discount,name='discount'),
    path('contact/',views.contact,name='contact'),
    path('booking/<int:pr_id>/',views.booking,name='booking'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('view_blog_detail/<int:pid>/',views.view_blog_detail,name='view_blog_detail'),
    path('signup/',views.user_sign,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('search/',views.search,name='search'),
    path('my_booking/',views.my_booking,name='my_booking'),
    path('details/<int:pr_id>/',views.detail,name='details'),
    path('delete_user/<int:pid>/',views.delete_user,name='delete_user'),
    path('delete_booking/<int:pid>/',views.delete_booking,name='delete_booking'),
    path('edit_destination/<int:pid>/',views.edit_destination,name='edit_destination'),
    path('payment/',views.Payment,name='payment'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('Change_Password/',views.Change_Password,name='Change_Password'),

    path('add_blog/',views.add_blog,name='add_blog'),
    path('delete_blog/<int:pid>',views.delete_blog,name='delete_blog'),
    path('admin_viewblog/',views.admin_viewblog,name='admin_viewblog'),
    path('view_contact/',views.view_contact,name='view_contact'),
    path('update_blog/<int:pid>',views.update_blog,name='update_blog'),
    path('view_booking/',views.view_booking,name='view_booking'),
    path('admin_delete_booking/<int:pid>/',views.admin_delete_booking,name='admin_delete_booking'),
    path('view_destination/',views.view_destination,name='view_destination'),
    path('delete_destination/<int:pid>/',views.delete_destination,name='delete_destination'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
