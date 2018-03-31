# DjangoFormGetStarted


# ��������
- ����ģ��
```
django-admin startproject mysite
```
- ����Ӧ��
```
python manage.py startapp blog
```

- �������ݱ�
```
python manage.py makemigrations
```
- ����Ǩ��
```
python manage.py migrate
```
- ���з���
```
python manage.py runserver
```
- ��Ӧ�ô������ݱ�
```
python manage.py makemigrations blog
```

# ���Ӧ�ô���

#### setting.py
- �����������Ŀ¼apps����apps ������message��Ӧ��
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


# ���Ը�Ϊ����
LANGUAGE_CODE = 'zh-hans'
# ʱ����Ϊ�Ϻ�
TIME_ZONE = 'Asia/Shanghai'
# ���ݿ�洢ʹ��ʱ�䣬Trueʱ��ᱻ��ΪUTC��ʱ��
USE_TZ = False
```

#### url.py
- �°汾��django ���治��Ҫ ����ƥ�䣬ֻ��Ҫ ��ʵ�ĵ�ַ���ɣ�
֮ǰ������
- Django 2.0.1�в���Ҫ��**r** Ҳ����Ҫ�� **^**
```
from django.conf.urls import url
path(r'^form/', getform, name="form_new"),

����
from django.urls import path
from message.views import getform
from message import views
path(r'form/', getform, name="form_new"),

����Ҳ����
path(r'form', getform, name="form_new"),
```

- �������ݿ���ʱ������
```
- python manage.py makemigrations messages 
```
- ���û����һ�� �����module ��������ݱ�����ʾ�� navacit ���棬�м�
- ֻ�в�������һ�����Ż��½� һ���� **message_usermessage** �ı�

- �����**models .py**����û�ж������� **object_id** ��ô����Ĭ�ϰ��� ԭ��������ID �Զ�������ÿ�μ�¼���Ḳ�ǣ�����Զ���������������ҳ�ϵ�������Ϣ���Ḳ��ǰһ�ε����ݣ���������ֻ��һ�����ԡ�

***
# ���xadmin ������
```
django-crispy-forms=1.6.0
django-import-export>=0.5.1
django-reversion~=2.0.0
django-formtools
future==0.15.2
httplib2==0.9.2
six==1.10.0

```

- ���̸�Ŀ¼�´���extra_apps���� �����ַ���� xadmin��Դ�룬������ **extra_apps** ����
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

- message Ŀ¼���� **adminx.py**
```
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import UserMessage


class MessageAdmin(object):
    list_display = ['name', 'email', 'address','message']  
	# ���������������Ժ�����һ��������
    search_fields = ['name', 'email', 'address']
	# ������������������һ������������
	list_filter =  ['name', 'email','address']

#modules class +��adminx class
xadmin.site.register(UserMessage, MessageAdmin)

```

- ��Ӵ���ʵ�ֿ�������Ĺ���
```
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)
```
- ��Ӵ���ʵ��xadmin �޸ı����Լ�ҳ�ŵ���ʾ�ַ�
```
class GlobalSettings(object):
    site_title = "Ľѧ��̨����ϵͳ"
    site_footer = "Ľѧ������"
    # menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSettings)
```

- ��Ӵ���Ϊ xadmin ����Ĳ˵��۵�

#### apps.py
```
from __future__ import unicode_literals

from django.apps import AppConfig


class MessageConfig(AppConfig):
    name = 'message'
    verbose_name = "�۵��˵�"
```
#### __init__.py

- ע����������� **message** �� **MessageConfig** Ҫһһ��Ӧ
default_app_config = "message.apps.MessageConfig"


***
# ���������û����������Ϊ��
```
python manage.py createsuperuser
```
- û�д��������û����һ��û����½



