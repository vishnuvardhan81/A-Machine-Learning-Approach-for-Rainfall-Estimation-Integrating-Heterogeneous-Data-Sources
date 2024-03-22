"""rainfall_estimation URL Configuration

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from Remote_User import views as remoteuser
from a_machine_learning_approach_for_rainfall_estimation import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Rainfall_Estimate_Prediction_Type/', remoteuser.Rainfall_Estimate_Prediction_Type, name="Rainfall_Estimate_Prediction_Type"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>/', serviceprovider.charts, name="charts"),
    path('charts1/<str:chart_type>/', serviceprovider.charts1, name="charts1"),
    path('likeschart/<str:like_chart>/', serviceprovider.likeschart, name="likeschart"),
    path('Find_Rainfall_Estimate_Prediction_Type_Ratio/', serviceprovider.Find_Rainfall_Estimate_Prediction_Type_Ratio, name="Find_Rainfall_Estimate_Prediction_Type_Ratio"),
    path('Train_Test_DataSets/', serviceprovider.Train_Test_DataSets, name="Train_Test_DataSets"),
    path('View_Rainfall_Estimate_Prediction_Type/', serviceprovider.View_Rainfall_Estimate_Prediction_Type, name="View_Rainfall_Estimate_Prediction_Type"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
