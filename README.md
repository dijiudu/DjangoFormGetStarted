# DjangoFormGetStarted


# 常用命令
- 创建模板
```
django-admin startproject mysite
```
- 创建应用
```
python manage.py startapp blog
```

- 建立数据表
```
python manage.py makemigrations
```
- 数据迁移
```
python manage.py migrate
```
- 运行服务
```
python manage.py runserver
```
- 给应用创建数据表
```
python manage.py makemigrations blog
```

# 添加应用代码

#### setting.py
- 如果创建了子目录apps，在apps 里面有message的应用
```
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'message',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
}


# 语言改为中文
LANGUAGE_CODE = 'zh-hans'
# 时区改为上海
TIME_ZONE = 'Asia/Shanghai'
# 数据库存储使用时间，True时间会被存为UTC的时间
USE_TZ = False
```

#### url.py
- 新版本的django 里面不需要 正则匹配，只需要 真实的地址即可，
之前的做法
- Django 2.0.1中不需要加**r** 也不需要加 **^**
```
from django.conf.urls import url
path(r'^form/', getform, name="form_new"),

现在
from django.urls import path
from message.views import getform
from message import views
path(r'form/', getform, name="form_new"),

这样也不行
path(r'form', getform, name="form_new"),
```

- 创建数据库表的时候命令
```
- python manage.py makemigrations messages 
```
- 如果没有这一步 会出现module 里面的数据表不会显示在 navacit 里面，切记
- 只有操作了这一步，才会新建 一个叫 **message_usermessage** 的表单

- 如果在**models .py**里面没有定义主键 **object_id** 那么表单是默认按照 原本的主键ID 自动自增，每次记录不会覆盖，如果自定义了主键，在网页上的留言信息都会覆盖前一次的数据，导致最终只有一个留言。

***
# 添加xadmin 到工程
```
django-crispy-forms=1.6.0
django-import-export>=0.5.1
django-reversion~=2.0.0
django-formtools
future==0.15.2
httplib2==0.9.2
six==1.10.0

```

- 工程根目录下创建extra_apps，从 下面地址下载 xadmin的源码，并放在 **extra_apps** 下面
```
https://github.com/mtianyan/xadmin_django2.0.1  
```

#### setting.py
```
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

INSTALLED_APPS = [
    'crispy_forms',
    'xadmin',
]

```
#### url.py
```
import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
```

- message 目录创建 **adminx.py**
```
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import UserMessage


class MessageAdmin(object):
    list_display = ['name', 'email', 'address','message']  
	# 添加下面这个代码以后会出来一个搜索框
    search_fields = ['name', 'email', 'address']
	# 添加下面这个代码会出来一个搜索过滤器
	list_filter =  ['name', 'email','address']

#modules class +　adminx class
xadmin.site.register(UserMessage, MessageAdmin)

```

- 添加代码实现开启主题的功能
```
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)
```
- 添加代码实现xadmin 修改标题以及页脚的显示字符
```
class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    # menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSettings)
```

- 添加代码为 xadmin 里面的菜单折叠

#### apps.py
```
from __future__ import unicode_literals

from django.apps import AppConfig


class MessageConfig(AppConfig):
    name = 'message'
    verbose_name = "折叠菜单"
```
#### __init__.py

- 注意这里的两个 **message** 和 **MessageConfig** 要一一对应
default_app_config = "message.apps.MessageConfig"


***
# 创建超级用户，邮箱可以为空
```
python manage.py createsuperuser
```
- 没有创建超级用户则第一次没法登陆



