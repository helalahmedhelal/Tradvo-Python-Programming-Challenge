from django.urls import path
from . import views

urlpatterns = [
    path('',views.interface,name='interface'),
    
    path('apk_list',views.apk_list,name='apk_list'),
    
    path('apk_add',views.apk_add,name='apk_add'),
    
    path('apk_details/<int:pk>/',views.apk_details,name='apk_details'),
    
    path('apk_update/<int:pk>/',views.apk_update,name='apk_update'),
    
    path('run_appium/<int:pk>/',views.run_appium,name='run_appium'),
    
    path('apk_delete/<int:pk>/',views.apk_delete,name='apk_delete'),
    

    
        
]