"""
api/contact.py — EducationalShaman contact form endpoint
POST /api/contact  →  saves to Upstash Redis
"""
import json
import time
import os
import urllib.request

UPSTASH_URL   = os.environ.get('UPSTASH_REDIS_REST_URL',  '')
UPSTASH_TOKEN = os.environ.get('UPSTASH_REDIS_REST_TOKEN', '')


def _redis(*cmd):
    """Execute a Redis command against Upstash."""
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


def handler(event, context):
    """Vercel serverless entry point."""
    from http.server import BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        pass

    # Parse the request
    method = event.get('request', {}).get('method', 'POST')
    if method != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'}),
        }

    try:
        body = json.loads(event.get('body', '{}'))
    except (json.JSONDecodeError, TypeError):
        # Try form-encoded
        try:
            from urllib.parse import parse_qs
            body = {k: v[0] for k, v in parse_qs(event.get('body', '')).items()}
        except Exception:
            body = {}

    name    = body.get('name', '').strip()
    email   = body.get('email', '').strip()
    message = body.get('message', '').strip()

    if not email or '@' not in email:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Valid email required'}),
        }

    submission = {
        'name':    name,
        'email':   email,
        'message': message,
        'ts':      int(time.time()),
    }

    # Store in Upstash — zset keyed by timestamp so we can range-query
    key = 'edusham:contacts'
    _redis('ZADD', key, str(int(time.time())), json.dumps(submission))

    print(f"[Contact] saved: {email}")
    return {
        'statusCode': 200,
        'body': json.dumps({'success': True}),
    }
