# Email OTP Authentication API 🔐

A Django-based API for user authentication using email and One-Time Password (OTP).

## Features
- User enters email to request an OTP.
- OTP is sent to the provided email.

  ##Tech Stack
- Django
- Django REST Framework

## 1. Request OTP
- **POST** `/emailapi/request-otp/`
- **Request Body:**
```json
{
  "email": "user@example.com"
}
