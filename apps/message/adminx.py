# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import UserMessage


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "后台管理系统演示版"
    site_footer = "演示版"
    # 收起菜单
    menu_style = "accordion"

class MessageAdmin(object):
    #排列顺序会影响显示顺序
    list_display = ['name', 'email', 'address','message']
    search_fields = ['name', 'email', 'address']
    list_filter =  ['name', 'email','address']

#modules class +　adminx class
xadmin.site.register(UserMessage, MessageAdmin)
# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

