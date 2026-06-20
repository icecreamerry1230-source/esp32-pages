import urllib.request
import json

token = "aef124964432a4d2fa7d680d473240d1"

# 尝试通过 Gitee OpenAPI 查看可用的服务/功能
urls = [
    f"https://gitee.com/api/v5/repos/icecreamerry/esp32-pages?access_token={token}",
    f"https://gitee.com/api/v5/repos/icecreamerry/esp32-pages/pages?access_token={token}",
]

for url in urls:
    try:
        r = urllib.request.urlopen(url)
        data = json.loads(r.read())
        print(f"\n=== {url.split('/')[-1].split('?')[0]} ===")
        # Print relevant fields
        for k in ['has_page', 'public', 'private', 'html_url', 'homepage', 'message']:
            if k in data:
                print(f"  {k}: {data[k]}")
    except Exception as e:
        print(f"\nError for {url}: {e}")
