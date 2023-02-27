import requests
import json

url = "https://protago-demo-chat-v3.ngrok.io/api/chatagent"

data = {
    "history": ["Hello, who are you?"],
    "is_suggestion": False,
}

headers = {
    "content-type": "application/json"
}

resp = requests.post(url=url, data=json.dumps(data), headers=headers)

print (resp)
print (json.loads(resp.text))
