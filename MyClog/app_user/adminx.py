import xadmin
from .models import BBSTopic,BBSUsers,BBSSecion,BBSReply
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "MyClog后台管理系统"
    site_footer = "TheShow"


class BBSUsersAdmin(object):
    list_display = ['id', 'UName', 'UPassword', 'UEmail','UBirthady','USex','UClass','UStatement','URegDate','UPoint']
    # search_fields = ['code', 'email', 'send_type']
    # list_filter = ['code', 'email', 'send_type', 'send_time']


class BBSSecionAdmin(object):
    list_display = ['id', 'SName', 'SMasterID', 'SStatement','SClickConut','STopicConut']
    # search_fields = ['code', 'email', 'send_type']
    # list_filter = ['code', 'email', 'send_type', 'send_time']


class BBSTopicAdmin(object):
    list_display = ['id', 'TSID', 'Tuid', 'TReplyCount', 'TTopic', 'TContents','TTime','TClickCount','is_delect']
    # search_fields = ['code', 'email', 'send_type']
    # list_filter = ['code', 'email', 'send_type', 'send_time']


class BBSReplyAdmin(object):
    list_display = ['id', 'RUserID', 'RTopicID', 'RContents', 'RMe']
    # search_fields = ['code', 'email', 'send_type']
    # list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)

xadmin.site.register(BBSUsers,BBSUsersAdmin)
xadmin.site.register(BBSSecion,BBSSecionAdmin)
xadmin.site.register(BBSTopic,BBSTopicAdmin)
xadmin.site.register(BBSReply,BBSReplyAdmin)
















