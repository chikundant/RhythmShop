from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail


@csrf_protect
def form_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = f'{request.POST.get("message")} + {email}'

        if email and subject and message:
            send_mail(subject, message, email, ['rhythm.manage@gmail.com'], fail_silently=False)
            return redirect('home')
    return render(request, 'contact_us/feedback.html')
    # success_url = 'home'
    # template_name = 'contact_us/feedback.html'
