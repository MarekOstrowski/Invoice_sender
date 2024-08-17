import base64
import requests
from config import API_KEY
from request_body import payload
import pypdf

order_number = 103640

url = "https://butomaniak.pl/api/admin/v3/orders/documents"
headers = {"accept": "application/json",
           "content-type": "application/json",
           "X-API-KEY": API_KEY}


with open(f"invoices/{order_number}.pdf", "rb") as pdf_file:
    reader = pypdf.PdfReader(pdf_file)
    page1 = reader.get_page(0)
    output_pdf = pypdf.PdfWriter()
    output_pdf.add_page(page1)
    output_pdf.write("first_page.pdf")
    pdf1page = open("first_page.pdf", "rb")
    encoded_string = base64.b64encode(pdf1page.read())
    encoded_string = encoded_string.decode("ascii")
    pdf1page.close()


payload = payload(order_number=order_number, pdfBase64=encoded_string)


response = requests.post(url, json=payload, headers=headers)

print(f'URL: {response.request.url}')
print(f'BODY: {response.request.body}')
print(f'HEADERS: {response.request.headers}')
print(f'RESPONSE: {response.text}')
print(f'STATUS CODE: {response.status_code}')
