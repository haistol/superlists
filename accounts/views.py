import uuid
import sys
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.core.mail import send_mail

from accounts.models import Token

def send_login_email(request):
    email = request.POST['email']
    uid = str(uuid.uuid4())
    Token.objects.create(email=email, uid=uid)
    print('saving uid', uid, 'for email', email, file = sys.stderr)
    url = request.build_absolute_uri(
        '/accounts/login?uid={uid}'.format(uid=uid)
        )
    send_mail(
        'Your logn link for Superlists',
        'Use this link to log in:\n\n{url}'.format(url=url),
        'noreply@dw48studio.tk',[email],
        )
    return render(request, 'login_email_sent.html')
    
def login(request):
    print('login view', file= sys.stderr)
    uid = request.GET.get('uid')
    if user is not None:
        auth_login(request, user)
        
    return redirect('/')
