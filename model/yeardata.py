import http.client
import json

def modelyeardata():
    conn = http.client.HTTPSConnection("data.covid19.go.id")
    payload = ''
    headers = {}
    conn.request("GET", "/public/api/update.json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    dataparse = json.loads(data)
    return data