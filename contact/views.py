from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings 


@login_required
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        try:
            send_mail(
                subject,
                f"Message from {email}: {message}",
                email,
                [settings.EMAIL_HOST_USER],  # or your personal email address
                fail_silently=False,
            )
            # Optionally add a success message or redirect
            return redirect('contact_success')
        except Exception as e:
            # Handle the error (log it or notify the user)
            print(f"Error sending email: {e}")

    context = {}
    return render(request, 'contact.html', context)



# @login_required
# def send_message(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         subject = request.POST.get('subject')
#         email = request.POST.get('email')

#         try:
#             send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,  # Optional: can be uncommented for error handling
#             )
#             # Optionally add a success message or redirect
#         except Exception as e:
#             # Handle the error (log it or notify the user)
#             print(f"Error sending email: {e}")

#     context = {}
#     return render(request, 'contact.html', context)
