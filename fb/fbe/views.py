#coding=utf-8
from django.shortcuts import render
from .models import Invitation
from .models import Oneword
import random
import smtplib
from email.mime.text import MIMEText
from django.template import RequestContext
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import datetime
from .models import Accept
# Create your views here.
def index(request):
	return render(request,'fbe/index.html',{
		'sex': request.COOKIES.get('sex') in ('0','1','2'),
	})#!!!
	#if not request.COOKIES.get('sex') in ('0', '1', '2'):
	#	return render(request,'fbe/index.html')#!!!
	#else:
	#	return redirect('toget', rd='2')

def _throw(request):
	return render(request,'fbe/tothrow.html')


def Throw(request):
	tp = request.POST.get('type')
	if tp == 1:
		sex=request.POST.get('o_sex')
		target=request.POST.get('target')
		email=request.POST.get('type1_email')
		#try:
		#	validate_email(email)
		#	return_data={
		#	'errcode':'0',
		#	}
		#	response=JsonResponse(return_data)
		#	return HttpResponse(response.content)
		#except ValidationError:
		#	return_data={
		#	'errcode':'1',
		#	}
		#	response=JsonResponse(return_data)
		#	return HttpResponse(response.content)
		content=request.POST.get('type1')
		i=Invitation(sex=sex,target=target,email=email,content=content)
		i.save()
	else:
		sex=request.POST.get('o_sex')
		target=request.POST.get('target')
		content=request.POST.get('type0')
		o = Oneword(sex=sex,target=target,oneword=content)
		o.save()
	return_data = {0}
	
	return render(request,'fbe/index.html')


def toget(request,rd):#??
	rd = int(rd)
	if not rd in (0, 1):
		rd = random.randint(0,1)
	if rd == 1:
		return render(request,'fbe/toget_invite.html')
	else:
		return render(request,'fbe/toget_sentence.html')

def pick(request):
	sex = request.POST.get('s_sex')#这里的request还能用吗？
	if not sex in ('0', '1', '2'):#checked
		return redirect('index')
	response = HttpResponse()
	if 'sex' not in request.COOKIES:
		response.set_cookie('sex', sex, max_age=172800)#2days
	return response
 
def picked(request):
	sex = request.COOKIES.get('sex')
	if not sex in ('0', '1', '2'):#checked
		return redirect('index')
	sex = int(sex)
	random_num=request.POST.get('type')
	try:
		random_num = int(random_num)
	except ValueError:
		random_num = 0
	if random_num==1:
		sex_chosed = Invitation.objects.filter(target=sex)
		alinv=sex_chosed.count()#快一點
		Random = random.randrange(alinv)
		random_i = sex_chosed[Random]
		random_sex = random_i.sex
		random_content = random_i.content
		random_email = random_i.email
		return_data={
			"o_sex":random_sex,
			"type1":random_content,
			"type1_email":random_email,
		}
		request.session["random_id"] = random_i.id
		request.session["random_email"] = random_email
		request.session["random_content"] = random_content
		#1.????????edited needed....
	else:
		sex_chosed = Oneword.objects.filter(target=sex)
		alow=sex_chosed.count()
		Random = random.randrange(alow)
		random_ow = sex_chosed[Random]
		random_sex = random_ow.sex
		random_oneword = random_ow.oneword
		return_data={
			"o_sex":random_sex,
			"type0":random_oneword,
		}
	#print 'id: ', sex_chosed[Random].id, random_num
	response = JsonResponse(return_data)
	return response

def email(request):
	random_email = request.session["random_email"]
	if request.method == 'GET':
		random_content = request.session["random_content"]
		#del request.session["random_email"]
		#del request.session["random_content"]
		return render( 
			request,
			'fbe/toget_invite_content.html',
			#{
			#	'email' : random_email,
			#	'content' : random_content,
			#},
		)
	accept_email = request.POST.get('s_email')
	try:
		validate_email(accept_email)
	except ValidationError:
		return_data={
		'error':'3',
		}
		return JsonResponse(return_data)
	ii = Invitation.objects.get(id=request.session["random_id"])
	#ii.accept_email = accept_email
	#p = Invitation.objects.filter(email = random_email)
	#q = any(x.accept_email == accept_email for x in list(p))
	#if q:
	try:
		Accept.objects.get(email=random_email, accept_email=accept_email)
	except Accept.DoesNotExist:
		pass
	else:
		return_data={
		'error':'2',
		}
		return JsonResponse(return_data)
	now = datetime.datetime.now()
	Accept(
		email=random_email,
		accept_email=accept_email,
		time=now
	).save()
	#ii.save()

	#发邮件

	try:
		email = EmailMessage(
    		u'漂流瓶小通知'.encode('utf-8'),
			(u'hey，同学！你扔的瓶子ta捡啦！ta的邮箱是'+ accept_email +u'。还愣啥?赶紧准备一下吧！（后台人员正在想象你们约会时的浪漫情景。奸笑ing。。）').encode('utf-8'),
			 'floatbottle@mail.sdu.edu.cn',
    		[random_email],
    		#reply_to=['another@example.com'],
    		headers={'Reply-To': accept_email},
		).send()

		#send_mail(u'漂流瓶小通知',
		#	u'hey，同学！你扔的瓶子ta捡啦！ta的邮箱是'+ accept_email +'。还愣啥?赶紧准备一下吧！（后台人员正在想象你们约会时的浪漫情景。奸笑ing。。）',
		#	 'floatbottle@mail.sdu.edu.cn',
    	#	[random_email],
    	# 	fail_silently=False,
     	#	)
	except smtplib.SMTPException:
		return_data={
		'error':'1',
		}
		return JsonResponse(return_data)
	else:
		#i = Invitation.objects.get(email = random_email)
		ii.time = now
		ii.save()
	return_data={
		'error':'0',
		}
	return JsonResponse(return_data)
#def prepick(request):
#	if 'sex' in request.COOKIES:
#		return render(request,'??')
#	else:
#		sex = request.POST.get('s_sex')
#		response = render_to_response(request,'??')
#		response.set_cookie('sex',sex)
#		return response

#def formView(request):#right
#	if 'sex' in request.COOKIES:
#		sex = request.COOKIES['sex']
#		return render(request,'??')
#    else:
#    	return render(request,'index.html')

def return_email(request):
	random_email = request.session["random_email"]
	random_content = request.session["random_content"]
	#del request.session["random_email"]
	#del request.session["random_content"]
	return JsonResponse(
		{
			'type1_email' : random_email,
			'type1' : random_content,
		}
	)

def login(request):
	passright='piaoliuping'
	tip=''
	password=request.session.get('password')
	if password!=None:
		if password!=passright:
			del request.session['password']
		else:
			return HttpResponseRedirect('/fbe/review/')
	else:
		if request.method=='POST':
			password=request.POST.get('password')
			if password!=passright:
				tip='口令错误'
			else:
				request.session['password']=password
				return HttpResponseRedirect('/fbe/review/')		
		else:
			pass
	return render(request, 'fbe/login.html', {
		'tip':tip,
	})

def logout(request):
	if request.session['password']!=None:
		del request.session['password']
	return HttpResponseRedirect('/fbe/login/')

def review(request):
	passright='piaoliuping'
	password=request.session.get('password')
	if password!=None:
		if password!=passright:
			del request.session['password']
			return HttpResponseRedirect('/fbe/login/')
		else:
			pass
	else:
		return HttpResponseRedirect('/fbe/login/')
	already=Invitation.objects.all()
	already1 = Oneword.objects.all()
	return render(request, 'fbe/review.html', {
		'already':already,
		'already1':already1,
	})


def in_cancel(request):
	cl = request.GET.get('id')
	Invitation.objects.get(id=cl).delete()
	return_data=0
	response=JsonResponse(return_data, safe=False)
	return HttpResponse(response.content)
	
def one_cancel(request):
	cl = request.GET.get('id')
	Oneword.objects.get(id=cl).delete()
	return_data=0
	response=JsonResponse(return_data, safe=False)
	return HttpResponse(response.content)