from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'projects.html')
def experience(request):
    return render(request,'experience.html')

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            # Extract form data (ensure keys match the form field names)
            name = data.get("name", "Anonymous")
            email = data.get("email", "No Email Provided")
            message = data.get("message", "")

            # Compose the email
            subject = f"Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = ["chaitanyalohani175@gmail.com"]  # Replace with your email address

            # Send the email
            send_mail(
                subject,
                body,
                "chaitanyalohani175@gmail.com",  # Sender email address
                recipient_list,
                fail_silently=False,
            )

            # Return a success response
            return JsonResponse({"message": "Email sent successfully!"}, status=200)

        except Exception as e:
            # Handle errors (e.g., invalid data, email sending failure)
            return JsonResponse({"message": str(e)}, status=400)

    return JsonResponse({"message": "Invalid request method"}, status=405)
