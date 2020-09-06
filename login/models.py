from django.db import models

# Create your models here.

#权限表
class Permission(models.Model):
    url=models.CharField(max_length=64)
    title=models.CharField(max_length=10)
    class Meta:
        verbose_name='权限表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(verbose_name=u"用户名",max_length=128, unique=True)
    password = models.CharField(verbose_name=u"密码",max_length=256)
    email = models.EmailField(verbose_name=u"邮箱",unique=True)
    mobile = models.CharField(verbose_name=u"联系电话",max_length=11, blank=True)
    address = models.CharField(verbose_name=u"家庭住址",max_length=100, default="")
    sex = models.CharField(verbose_name=u"性别",max_length=32, choices=gender, default="男")
    age = models.CharField(verbose_name=u"年龄",max_length = 2)
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)
    permission = models.ManyToManyField(Permission, null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"