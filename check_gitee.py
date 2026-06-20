import urllib.request
import json

token = "aef124964432a4d2fa7d680d473240d1"

# Check user email/verification status
r = urllib.request.urlopen(f"https://gitee.com/api/v5/user?access_token={token}")
user = json.loads(r.read())

print("=== Account Info ===")
for k in ['login', 'name', 'email', 'created_at', 'updated_at', 'blog', 'bio']:
    print(f"  {k}: {user.get(k)}")

print(f"  public_repos: {user.get('public_repos')}")
print(f"  followers: {user.get('followers')}")

# Check emails
try:
    r2 = urllib.request.urlopen(f"https://gitee.com/api/v5/emails?access_token={token}")
    emails = json.loads(r2.read())
    print(f"\nEmails: {emails}")
except Exception as e:
    print(f"\nEmail check error: {e}")
