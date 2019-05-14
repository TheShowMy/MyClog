from django.db import models
# Create your models here.


# 用户模型
class BBSUsers(models.Model):
    # null=True,blank=True 需要为空值是添加
    STATUS_CHOICES = (('男', '1'), ('女', '2'),('保密', '3'),)
    UName = models.CharField(max_length=12,verbose_name='用户名')
    UPassword = models.CharField(max_length=50,verbose_name='用户密码')
    UEmail = models.CharField(max_length=100,verbose_name='Email')
    UBirthady = models.DateTimeField()
    USex = models.CharField(max_length=10,choices=STATUS_CHOICES,default='保密',verbose_name='性别')
    UClass = models.IntegerField(default=0,verbose_name='等级')
    UStatement = models.CharField(max_length=200,null=True,blank=True,verbose_name='签名')
    URegDate = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    UPoint = models.IntegerField(default=0,verbose_name='用户积分')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.UName


# 板块模型
class BBSSecion(models.Model):
    SName = models.CharField(max_length=50,verbose_name='板块名称')
    SMasterID = models.ForeignKey('BBSUsers',verbose_name='版主id')
    SStatement = models.CharField(max_length=200,verbose_name='版块说明')
    SClickConut = models.IntegerField(default=0,verbose_name='版块点击次数')
    STopicConut = models.IntegerField(default=0,verbose_name='版块帖子数')

    class Meta:
        verbose_name = '版块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.SName


# 帖子模型
class BBSTopic(models.Model):
    TSID = models.ForeignKey('BBSSecion',verbose_name='贴子板块编号')
    Tuid = models.ForeignKey('BBSUsers',verbose_name='贴子用户编号')
    TReplyCount = models.IntegerField(default=0,verbose_name='贴子回复次数')
    TTopic = models.CharField(max_length=100,verbose_name='贴子标题')
    TContents = models.TextField(verbose_name='贴子内容')
    TTime = models.DateTimeField(auto_now_add=True,verbose_name='发贴时间')
    TClickCount = models.IntegerField(default=0,verbose_name='贴子点击次数')
    is_delect = models.BooleanField(verbose_name='是否删除')

    class Meta:
        verbose_name = '贴子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.TTopic


# 评论模型
class BBSReply(models.Model):
    RUserID = models.ForeignKey('BBSUsers',verbose_name='评论用户id')
    RTopicID = models.ForeignKey('BBSTopic',verbose_name='贴子ID')
    RContents = models.TextField(verbose_name='评论内容')
    RMe = models.ForeignKey('self',verbose_name='父级评论',default=None,null=True,blank=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.RContents