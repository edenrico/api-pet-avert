import requests
import json


payload = json.dumps({
  "CodigoInterno": "395470"
})
             
api_url = "https://apiwebservices.biolabfarma.com.br/api/Dynamic/produtosDev"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiKiogVXNvIGV4Y2x1c2l2byBwYXJhIGEgQVBJIEJpb2xhYiAqKiIsImV4cCI6MTg4MzY2ODM2NSwiaXNzIjoiQmlvbGFiIEZhcm1hY2V1dGljYSIsImF1ZCI6IkJpb2xhYiBGYXJtYWNldXRpY2EifQ.Me6R1DdyK3qX_O0-diuijd4CMT4dtodSF4XWNFg5F2s"
}

response = requests.get(api_url, headers=headers, data=payload)

if response.status_code == 200:
    # deu tudo certo
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
