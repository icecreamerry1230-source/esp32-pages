import urllib.request
import json

token = "aef124964432a4d2fa7d680d473240d1"

# Check repo info
r = urllib.request.urlopen(f"https://gitee.com/api/v5/repos/icecreamerry/esp32-pages?access_token={token}")
repo = json.loads(r.read())
print(f"public: {repo['public']}")
print(f"has_page: {repo['has_page']}")
print(f"default_branch: {repo['default_branch']}")

# Check user info
r2 = urllib.request.urlopen(f"https://gitee.com/api/v5/user?access_token={token}")
user = json.loads(r2.read())
print(f"user: {user['login']}")
print(f"created: {user['created_at']}")
