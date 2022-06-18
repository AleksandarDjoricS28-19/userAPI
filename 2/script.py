import http.client
import json

conn = http.client.HTTPConnection("localhost", 8081)
payload = json.dumps({
  "ime": "Aleksandar",
  "prezime": "Djoric",
  "username": "adjoric",
  "predmeti": [
    {
      "ime": "C#",
      "espb": 8
    },
    {
      "ime": "RVAS",
      "espb": 4
    }
  ],
  "smer": "IT"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))