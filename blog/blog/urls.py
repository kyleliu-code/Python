"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

# 在导入的时候，import 后面只能跟文件对象或者 python 中的对象（一般是类名或者方法）

# 貌似blog 指的就是管理文件 (内部的)blog,外部只是一个环境， 全局作用域

from blog.article import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$',views.add),
    # 请求的 url 和对应的处理方法
    url(r'^list/$',views.list),
    url(r'^view/(?P<id>\d+)$',views.view),
    url(r'^comment/add/$',views.comment_add),
]
