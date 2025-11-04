""" ============== Imports ================ """
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

""" ================== Email View =================== """
def contact_us(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New message from {user_name}"
        full_message = f"""
You have received a new message from your website contact form:

Name: {user_name}
Email: {user_email}

Message:
{message}
"""

        #  1. Send message to you (admin)
        print("Sending email to admin and user...")

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ["nomandev769@gmail.com"],  # 👈 your email
        )

        #  2. Send confirmation email to user
        send_mail(
            "Thanks for contacting us!",
            f"Hi {user_name},\n\nWe received your message and will reply soon.\n\nYour message:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
        )

        return render(request, "thanks/thank_you.html", {"name": user_name})

    return render(request, "contact_us/contact_us.html")
