import base64
import requests
from config import API_KEY
from request_body import payload

order_number = 103627

url = "https://butomaniak.pl/api/admin/v3/orders/documents"
headers = {"accept": "application/json",
           "content-type": "application/json",
           "X-API-KEY": API_KEY}


with open(f"invoices/{order_number}.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    encoded_string = encoded_string.decode("ascii")


payload = payload(order_number=order_number, pdfBase64=encoded_string)


response = requests.post(url, json=payload, headers=headers)

print(f'URL: {response.request.url}')
print(f'BODY: {response.request.body}')
print(f'HEADERS: {response.request.headers}')
print(f'RESPONSE: {response.text}')
print(f'STATUS CODE: {response.status_code}')
