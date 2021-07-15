"""onlineCompititiveExaminationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from OCES import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('take_test/',views.take_test),
    path('about_us/',views.about_us),
    path('contact_us/',views.contact_us),
    # path('start_test/',views.questionPaper),
    path('take_test/start_test/',views.start_test),
    path('take_test/start_test/questionPaper/',views.questionPaper),
    path('take_test/start_test/questionPaper/save_answers/',views.save_answers),
    path('take_test/start_test/questionPaper/check_queN/',views.check_que_num),

    
]
