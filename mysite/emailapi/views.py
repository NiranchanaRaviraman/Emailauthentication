from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import EmailVerify
from django.core.mail import send_mail
import random

class RequestOTPView(APIView): 
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'}, status=400)

        
        if EmailVerify.objects.filter(email=email).exists():
            return Response({'message': 'Email already registered'})

        otp = str(random.randint(100000, 999999))
        EmailVerify.objects.create(email=email, otp=otp)

        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            'no-reply@example.com',  
            [email],
            fail_silently=False,
        )

        return Response({'message': 'OTP sent to your email.'})
