import requests

w = (input("give the website :"))
x = requests.get(w)
# x = requests.get("https://accuknox.com")
print(f"Status Code: {x.status_code}")

if x.status_code == 200:
    print("✅ website is healthy")
else:
    print("⚠️not healthy")

#--------------------------------------------
# #!/bin/bash

# URL="https://accuknox.com"

# # Send a request and capture the HTTP status code
# STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

# echo "Status Code: $STATUS"

# if [ "$STATUS" -eq 200 ]; then
#     echo "✅ Website is healthy"
# else
#     echo "⚠️ Website is not healthy"
# fi