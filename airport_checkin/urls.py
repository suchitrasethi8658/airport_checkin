from django.contrib import admin
from passenger import views as passenger_views
from management import views as management_views
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', passenger_views.login, name="login"),
    path('register/', passenger_views.register, name="register"),
    path('mydetails/', passenger_views.mydetails, name="mydetails"),
    path('updata_details/', passenger_views.updata_details, name="updata_details"),
    path('view_checkin/', passenger_views.view_checkin, name="view_checkin"),
    re_path(r'^feedback/(?P<pk>\d+)/', passenger_views.feedback, name="feedback"),
    path('adminlogin/', management_views.adminlogin, name="adminlogin"),
    path('upload_airport/', management_views.upload_airport, name="upload_airport"),
    path('view_upload/', management_views.view_upload, name="view_upload"),
    path('view_feedback/', management_views.view_feedback, name="view_feedback"),
    re_path(r'^chart_page/(?P<chart_type>\w+)', management_views.chart_page, name="chart_page"),
    re_path(r'^country_chart/(?P<chart_type1>\w+)', management_views.country_chart, name="country_chart"),
    re_path(r'^pass_chart/(?P<chart_type2>\w+)', management_views.pass_chart, name="pass_chart"),
]
