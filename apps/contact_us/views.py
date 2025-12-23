from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs
# Create your views here.

def contact_us(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_email = request.POST.get("email")
        message = request.POST.get("message")

        if not user_name or not user_email or not message:
            return JsonResponse({"status": "error", "message": "All fields are required."})

        try:
            ContactUs.objects.create(name=user_name, email=user_email, message=message)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        


        subject = f"New message from {user_name}"
        full_message = f"""
You have received a new message from your website contact form:

Name: {user_name}
Email: {user_email}

Message:
{message}
"""

        try:
            # Send to admin
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])

            # Send confirmation to user
            send_mail(
                "Thanks for contacting us!",
                f"Hi {user_name},\n\nWe received your message and will reply soon.\n\nYour message:\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
            )

            return JsonResponse({"status": "success", "name": user_name})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "contact_us/contact_us.html")

def faqs(request):
    return render(request, 'faqs/faqs.html')

def privacy_policy(request):
    return render(request, "faqs/privacy_policy.html")
    
def term_of_use(request):
    return render(request, "faqs/term_of_use.html")
