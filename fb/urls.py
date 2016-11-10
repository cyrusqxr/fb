"""fb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from fbe import views
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^fb/$',views.index, name='index'), 
	url(r'^fbe/invitation/$',views.Invitation,name='invitation'), 
	url(r'^fbe/pick/$',views.pick,name='pick'),
	url(r'^fbe/return_email/$',views.return_email,name='return_email'), 
	url(r'^fbe/toget/(?P<rd>[0-9]+)/$',views.toget,name='toget'),
	url(r'^fbe/picked/$',views.picked,name='picked'),
	url(r'^fbe/email/$',views.email,name='email'),
	url(r'^fbe/throw/$',views.Throw,name='Throw'),
	url(r'^fbe/_throw/$',views._throw,name='_throw'),
	url(r'^fbe/review/$',views.review,name='review'),
    url(r'^fbe/login/$',views.login,name='login'),
    url(r'^fbe/logout/$',views.logout,name='logout'),
    url(r'^fbe/in_cancel/$',views.in_cancel,name='in_cancel'),
    url(r'^fbe/one_cancel/$',views.one_cancel,name='one_cancel'),
    #url(r'^news.html/$',views.news,name='news'),
    ]
