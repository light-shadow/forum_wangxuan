# coding:utf-8
import datetime
import uuid

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from models import ActivateCode

# Create your views here.


def register(request):
    error = ""
    if request.method == "GET":
        return render_to_response("usercenter_register.html", {},
                                 context_instance=RequestContext(request))
    else:
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"].strip()
        re_password = request.POST["re_password"].strip()
        if not username or not email:
            error = u"任何字段都不能为空！"
        if password != re_password:
            error = u"两次输入的密码不一致！"
        if User.objects.filter(username=username).count() > 0:
            error = u"用户已存在！"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).repalce("-", "")
            expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
            code_record = ActivateCode(owner=user, code=new_code(), expire_timestamp=expire_time)
            code_record.save()
            activate_link = "http://%s%s" % (request.get_host(), reverse("usercenter_activate", args=[new_code]))
            send_mail(u"[python部落]激活邮件", u"您的激活码为:%s" % activate_link, "wangxuan8901@126.com", [email], fail_silently=False)
        else:
            return render_to_response("usercenter_register.html", {"error": error},
                                      context_instance=RequestContext(request))
        return redirect(reverse("login"))


def activate(request, code):
    query = ActivateCode.objects.filter(code=code, expire_time_stamp_gte=datetime.datetime.now())
    if query > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return HttpResponse(u"激活成功")
    else:
        return HttpResponse(u"激活失败")
