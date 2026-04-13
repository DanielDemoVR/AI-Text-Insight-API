import requests
import threading

# Replace with your actual Endpoint ID and API Key from RunPod console
ENDPOINT_ID = "YOUR_ENDPOINT_ID"
API_KEY = "rpa_JL2P9IJJC0O6BZ9E7FH1ZYSF237TF22056L0WXIAay0a5i"

URL = f"https://api.runpod.ai/v2/{ENDPOINT_ID}/run"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def send_request(i):
    data = {"input": {"text": f"Task number {i}"}}
    response = requests.post(URL, json=data, headers=HEADERS)
    print(f"Request {i} sent: {response.status_code}")

# Launch 20 concurrent threads to show instant scaling
for i in range(20):
    threading.Thread(target=send_request, args=(i,)).start()