"""
api/index.py — Mindwright.ai API
POST /api/contact  →  sends email via SendGrid
"""
import json
import os
import urllib.request
import urllib.error
from flask import Flask, request, jsonify

app = Flask(__name__)

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')
TO_EMAIL         = os.environ.get('CONTACT_TO_EMAIL', 'eugene@mindwright.ai')
FROM_EMAIL       = os.environ.get('CONTACT_FROM_EMAIL', 'eugene@mindwright.ai')
FROM_NAME        = 'Mindwright.ai Contact Form'


def _send_email(name: str, email: str, interest: str, message: str) -> bool:
    """Send a contact notification via SendGrid Web API v3."""
    if not SENDGRID_API_KEY:
        print('[SendGrid] SENDGRID_API_KEY not set — skipping email')
        return False

    subject = f'Mindwright inquiry: {interest or "General"} — {name or email}'
    body = (
        f'Name:     {name or "(not provided)"}\n'
        f'Email:    {email}\n'
        f'Interest: {interest or "(not specified)"}\n\n'
        f'Message:\n{message or "(no message)"}\n'
    )

    payload = json.dumps({
        'personalizations': [{'to': [{'email': TO_EMAIL}]}],
        'from': {'email': FROM_EMAIL, 'name': FROM_NAME},
        'reply_to': {'email': email, 'name': name or email},
        'subject': subject,
        'content': [{'type': 'text/plain', 'value': body}],
    }).encode()

    req = urllib.request.Request(
        'https://api.sendgrid.com/v3/mail/send',
        data=payload,
        method='POST',
    )
    req.add_header('Authorization', f'Bearer {SENDGRID_API_KEY}')
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f'[SendGrid] sent to {TO_EMAIL}, status {resp.status}')
            return True
    except urllib.error.HTTPError as e:
        body_bytes = e.read()
        print(f'[SendGrid] HTTP {e.code}: {body_bytes.decode(errors="replace")}')
        return False
    except Exception as e:
        print(f'[SendGrid] error: {type(e).__name__}: {e}')
        return False


@app.route('/api/contact', methods=['POST'])
def contact():
    data     = request.get_json(force=True) or {}
    name     = data.get('name', '').strip()
    email    = data.get('email', '').strip()
    interest = data.get('interest', '').strip()
    message  = data.get('message', '').strip()

    if not email or '@' not in email:
        return jsonify({'error': 'Valid email required'}), 400

    ok = _send_email(name, email, interest, message)
    if not ok:
        print(f'[Contact] UNSENT — name={name!r} email={email!r} interest={interest!r}')

    print(f'[Contact] received from {email}, interest={interest!r}')
    return jsonify({'success': True})


# Vercel WSGI entry point
try:
    from vercel.wsgi import Vercel
    app = Vercel(app)
except ImportError:
    pass
