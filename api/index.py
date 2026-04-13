"""
api/index.py — EducationalShaman API
POST /api/contact  →  saves contact form submission to Upstash Redis
"""
import json
import time
import os
import urllib.request
from flask import Flask, request, jsonify

app = Flask(__name__)

UPSTASH_URL   = os.environ.get('UPSTASH_REDIS_REST_URL',  '')
UPSTASH_TOKEN = os.environ.get('UPSTASH_REDIS_REST_TOKEN', '')


def _redis(*cmd):
    if not UPSTASH_URL or not UPSTASH_TOKEN:
        return None
    payload = json.dumps([list(cmd)]).encode()
    req = urllib.request.Request(
        f"{UPSTASH_URL}/pipeline", data=payload, method='POST'
    )
    req.add_header('Authorization', f'Bearer {UPSTASH_TOKEN}')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read())[0].get('result')
    except Exception as e:
        print(f"[Redis error] {type(e).__name__}: {e}")
        return None


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True) or {}
    name    = data.get('name', '').strip()
    email   = data.get('email', '').strip()
    message = data.get('message', '').strip()

    if not email or '@' not in email:
        return jsonify({'error': 'Valid email required'}), 400

    submission = {
        'name':    name,
        'email':   email,
        'message': message,
        'ts':      int(time.time()),
    }

    _redis('ZADD', 'edusham:contacts', str(int(time.time())), json.dumps(submission))
    print(f"[Contact] saved: {email}")

    return jsonify({'success': True})


# Vercel WSGI entry point
try:
    from vercel.wsgi import Vercel
    app = Vercel(app)
except ImportError:
    pass
